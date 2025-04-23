import json
import sqlite3
import logging
from logger import setup_logger
setup_logger()
DATABASE = "WHITEHAT.db"

def load_attack_data():
    with open("attack-stix-data/enterprise-attack/enterprise-attack.json", "r", encoding="utf-8") as file:
        enterprise_attack_data = json.load(file)
    with open("attack-stix-data/ics-attack/ics-attack.json", "r", encoding="utf-8") as file:
        ics_attack_data = json.load(file)
    with open("attack-stix-data/mobile-attack/mobile-attack.json", "r", encoding="utf-8") as file:
        mobile_attack_data = json.load(file)
    return [enterprise_attack_data, ics_attack_data, mobile_attack_data]

def insert_data_to_MITREATTACK_Tables():
    attack_files = load_attack_data()

    try:
        with sqlite3.connect(DATABASE) as connection:
            cursor = connection.cursor()

            for attack_data in attack_files:
                for obj in attack_data["objects"]:
                    if obj.get("type") == "attack-pattern":
                        technique_id = obj.get("id")
                        techniqueName = obj.get("name")
                        description = obj.get("description")
                        

                    # Insert ExternalReferences
                    for reference in obj.get("external_references", []):
                        source = reference.get("source_name")
                        url = reference.get("url")
                        ref_description = reference.get("description")
                        try:
                            external_id = reference.get("external_id")
                        except KeyError:
                            external_id = None
                        
                                
                      
                        cursor.execute('''
                            INSERT OR IGNORE INTO ExternalReferences (external_id)
                            VALUES (?)
                        ''', (external_id,))

            connection.commit()
            logging.info("✅ MITRE ATT&CK data inserted successfully.")

    except sqlite3.OperationalError as e:
        logging.error(f"SQLite error: {e}")
    except Exception as e:
        logging.error(f"Error: {e}")
    finally:
        connection.close()
insert_data_to_MITREATTACK_Tables()