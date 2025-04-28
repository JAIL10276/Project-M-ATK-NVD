import requests
import time
import sqlite3
import os
from datetime import datetime, timedelta, timezone
import logging
# Set up logging configuration
from logger import setup_logger
setup_logger()

# Function to get the last update timestamp from a file
def get_last_update(filename="last-sync.txt"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return file.read().strip()
    return None
# Configuration
NVDAPIURL = "https://services.nvd.nist.gov/rest/json/cves/2.0"
DATABASE = "project-src/database/WHITEHAT.db"
NVDAPIKEY = '4c13a7c8-d650-40af-975c-aad7ed9200c5'  # Replace with your actual API key
# Note: The API key should be kept secret and not hardcoded in production code.
HEADERS = {"apiKey": NVDAPIKEY}
RESULTS_PER_PAGE = 2000
# Calculate the date window
today = (datetime.now(timezone.utc)- timedelta(days=2))
three_days_ago = today - timedelta(days=2)

#LASTMOD_START_DATE = three_days_ago.strftime("%Y-%m-%dT%H:%M:%S.000Z")
#LASTMOD_END_DATE = today.strftime("%Y-%m-%dT%H:%M:%S.000Z")


# Importing the ChunkedEncodingError exception for handling chunked responses
from requests.exceptions import ChunkedEncodingError

# Function to handle requests with retries
def safe_request(url, headers, params, retries=5, delay=10):
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response
        except ChunkedEncodingError:
            logging.error(f"⚠️ ChunkedEncodingError, retrying in {delay} seconds... (attempt {attempt + 1})")
            time.sleep(delay)
        except requests.RequestException as e:
            logging.error(f"⚠️ Other Request Error: {e}")
            time.sleep(delay)
    raise Exception("❌ Failed to fetch after retries")

# Function to insert data into NVD tables
def insert_data_to_NVD_Tables():
    start_time = time.time()
    start_index = 260000
    total_inserted = 0

    try:
        with sqlite3.connect(DATABASE) as connection:
            logging.info("✅ Connected to SQLite DB")
            cursor = connection.cursor()

            while True:
                logging.info(f"\n📦 Fetching vulnerabilities starting at index {start_index}...")

                params = {
                    "resultsPerPage": RESULTS_PER_PAGE,
                    "startIndex": start_index,
                    #"lastModStartDate": LASTMOD_START_DATE,
                    #"lastModEndDate": LASTMOD_END_DATE
                }

                response = safe_request(NVDAPIURL, headers=HEADERS, params=params)

                if response.status_code != 200:
                    logging.error(f"❌ Request failed: {response.status_code}")
                    logging.error(f"Response: {response.text}")
                    break

                data = response.json()
                vulnerabilities = data.get("vulnerabilities", [])

                if not vulnerabilities:
                    logging.info("✅ No more vulnerabilities to fetch.")
                    break

                logging.info(f"Retrieved {len(vulnerabilities)} vulnerabilities.")

                for vulnerability in vulnerabilities:
                    cve = vulnerability.get("cve", {})
                    cve_id = cve.get("id")

                    if not cve_id:
                        continue

                    # --- Insert CVE ---
                    source_identifier = cve.get("sourceIdentifier")
                    published = cve.get("published")
                    last_modified = cve.get("lastModified")
                    vuln_status = cve.get("vulnStatus")
                    description = next((d.get("value") for d in cve.get("descriptions", []) if d.get("lang") == "en"), "")

                    cursor.execute('''
                        INSERT OR IGNORE INTO CVE (CVE_ID, sourceIdentifier, published, lastModified, vulnStatus, description)
                        VALUES (?, ?, ?, ?, ?, ?)
                    ''', (cve_id, source_identifier, published, last_modified, vuln_status, description))

                    # --- Insert Tags ---
                    tags_field = cve.get("cveTags", [])

                    if isinstance(tags_field, list):
                        for tag_obj in tags_field:
                            if isinstance(tag_obj, dict):
                                tags_list = tag_obj.get("tags", [])
                                for single_tag in tags_list:
                                    cursor.execute('''
                                        INSERT OR IGNORE INTO CVETags (CVE_ID, Tags)
                                        VALUES (?, ?)
                                    ''', (cve_id, single_tag))
                            elif isinstance(tags_field, dict):
                                tags_list = tags_field.get("tags", [])
                                for single_tag in tags_list:
                                    cursor.execute('''
                                        INSERT OR IGNORE INTO CVETags (CVE_ID, Tags)
                                        VALUES (?, ?)
                                    ''', (cve_id, single_tag))
                            elif isinstance(tags_field, str):
                                cursor.execute('''
                                    INSERT OR IGNORE INTO CVETags (CVE_ID, Tags)
                                    VALUES (?, ?)
                                ''', (cve_id, tags_field))

                    # --- Insert Metrics and CVSSData ---
                    for metric in cve.get("metrics", {}).get("cvssMetricV2", []):
                        source = metric.get("source")
                        type_ = metric.get("type")
                        cvss_data = metric.get("cvssData", {})

                        if cvss_data:
                            version = cvss_data.get("version")
                            cve_id = cve.get("id")
                            # Insert into CVSSData
                            cvss_id = f"CVSS-{cve_id}-{version}"
                            cursor.execute('''
                                INSERT OR IGNORE INTO CVSSData (CVE_ID, CVSS_ID, version, vectorString, baseScore, accessVector, accessComplexity, authentication, confidentialityImpact, integrityImpact, availabilityImpact)
                                VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                            ''', (
                                cve_id,
                                cvss_id,
                                cvss_data.get("version"),
                                cvss_data.get("vectorString"),
                                cvss_data.get("baseScore"),
                                cvss_data.get("accessVector"),
                                cvss_data.get("accessComplexity"),
                                cvss_data.get("authentication"),
                                cvss_data.get("confidentialityImpact"),
                                cvss_data.get("integrityImpact"),
                                cvss_data.get("availabilityImpact")
                            ))

                            # Insert into Metrics
                            cursor.execute('''
                                INSERT OR IGNORE INTO Metrics (CVE_ID, source, type, CVSS_ID, baseSeverity, exploitabilityScore, impactScore, acInsufInfo, obtainAllPrivilege, obtainUserPrivilege, obtainOtherPrivilege, userInteractionRequired)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                            ''', (
                                cve_id,
                                source,
                                type_,
                                cvss_id,
                                metric.get("baseSeverity"),
                                metric.get("exploitabilityScore"),
                                metric.get("impactScore"),
                                metric.get("acInsufInfo"),
                                metric.get("obtainAllPrivilege"),
                                metric.get("obtainUserPrivilege"),
                                metric.get("obtainOtherPrivilege"),
                                metric.get("userInteractionRequired")
                            ))

                    # --- Insert Weaknesses ---
                    for weakness in cve.get("weaknesses", []):
                        source = weakness.get("source")
                        type_ = weakness.get("type")
                        for desc in weakness.get("description", []):
                            if desc.get("lang") == "en":
                                cwe_id = desc.get("value")
                                is_classified = 1 if cwe_id.startswith("CWE-") else 0
                                cursor.execute('''
                                    INSERT OR IGNORE INTO Weaknesses (CVE_ID, source, type, CWE_ID, isClassified)
                                    VALUES (?, ?, ?, ?, ?);
                                ''', (cve_id, source, type_, cwe_id, is_classified))

                    # --- Insert Configurations ---
                    configurations = cve.get("configurations", {})

                    nodes = []
                    if isinstance(configurations, dict):
                        nodes = configurations.get("nodes", [])
                    elif isinstance(configurations, list):
                        for item in configurations:
                            if isinstance(item, dict):
                                nodes.extend(item.get("nodes", []))
                    else:
                        nodes = []

                    # Now safe to iterate
                    for node in nodes:
                        if isinstance(node, dict):
                            operator = node.get("operator")
                            # process normally
                        else:
                            logging.error(f"⚠️ Unexpected node format, skipping: {node}")

                        cve_id = cve.get("id")
                        operator = node.get("operator")
                        negate = node.get("negate")
                        vuln_status = node.get("vulnerable")
                        for match in node.get("cpeMatch", []):
                            if match.get("vulnerable"):
                                match_criteria_id = match.get("matchCriteriaId")
                                criteria = match.get("criteria")
                                cursor.execute('''
                                    INSERT OR IGNORE INTO Configurations (CVE_ID, operator, negate, CPEMatch_ID)
                                    VALUES (?, ?, ?, ?)
                                ''', (cve_id, operator, negate, match_criteria_id))
                                cursor.execute('''
                                    INSERT OR IGNORE INTO CPEMatch (CVE_ID, CPEMatch_ID, vulnerable, criteria, matchCriteria_ID)
                                    VALUES (?, ?, ?, ?, ?)
                                ''', (cve_id, match_criteria_id, vuln_status, criteria, match_criteria_id))

                    # --- Insert References ---
                    for reference in cve.get("references", []):
                        url = reference.get("url")
                        source = reference.get("source")
                        cursor.execute('''
                            INSERT OR IGNORE INTO SecurityControls (CVE_ID, url, source)
                            VALUES (?, ?, ?)
                        ''', (cve_id, url, source))

                    total_inserted += 1

                    # --- Insert into CVE_CWE_Mapping ---
                    for weakness in cve.get("weaknesses", []):
                        if isinstance(weakness.get("description", [{}]), dict):
                             cwe_id = weakness.get("description", [{}]).get("value")
                        else:
                            cwe_id = weakness.get("description", [{}])[0].get("value")
                        if cwe_id:
                            if cwe_id.startswith("CWE-"):
                                cursor.execute('''
                                    INSERT OR IGNORE INTO CVE_CWE_Mapping (CVE_ID, CWE_ID)
                                    VALUES (?, ?)
                                ''', (cve_id, cwe_id))
                            else:
                                cursor.execute('''
                                    INSERT OR IGNORE INTO CVE_CWE_Mapping (CVE_ID, CWE_ID)
                                    VALUES (?, ?)
                                ''', (cve_id, "unknown"))
                connection.commit()
                logging.info(f"✅ Inserted {len(vulnerabilities)} vulnerabilities")

                start_index += RESULTS_PER_PAGE
                time.sleep(10)

            logging.info(f"\n🏁 Finished inserting all vulnerabilities. Total inserted: {total_inserted}")
    # Handle exceptions
    except sqlite3.OperationalError as e:
        logging.error(f"SQLite error: {e}")
    except requests.RequestException as e:
        logging.error(f"Request error: {e}")
    except Exception as e:
        logging.error(f"General error: {e}")
    finally:
        connection.close()
        end_time = time.time()
        elapsed_time = end_time - start_time
        minutes, seconds = divmod(elapsed_time, 60)
        logging.info(f"\n⏱️ Elapsed Time: {int(minutes)} minutes {int(seconds)} seconds")
        save_last_update(datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z"))
        logging.info(f"✅ Task Finished at {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.000Z')}, saved to last-sync.txt")
# Function to save the last update timestamp to a file
def save_last_update(timestamp: str, filename="last-sync.txt"):
    with open(filename, "w") as file:
        file.write(timestamp)


'''
# Example usage and time taken from the last run

🏁 Finished inserting all vulnerabilities. Total inserted: 291023

⏱️ Elapsed Time: 48 minutes 11 seconds
✅ NVD data parsed successfully.
'''