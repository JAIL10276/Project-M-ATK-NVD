import NVDAPI
import MITREATTACKAPI
import ConnSQLite
import logging
from datetime import datetime
# Set up logging configuration
from logger import setup_logger
setup_logger()
# MITRE ATT&CK and NVD Parser
# This script is designed to parse data from NVD and MITRE ATT&CK APIs and store it in a SQLite database.
# It includes functions to create the database, parse data, and save the last update time.
logging.basicConfig(filename="logs.txt",level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Starting the script...")

def create_database():
    try:
        logging.info("Creating database...")
        ConnSQLite.create_database()
        logging.info("✅ Database and tables created successfully.")
    except Exception as e:
        logging.error(f"❌ Error during database creation: {e}")
def parse_NVD_data_to_database():
    try:
        logging.info("🔵 Parsing NVD data...")
        NVDAPI.insert_data_to_NVD_Tables()
        logging.info("✅ NVD data parsed successfully.")
    except Exception as e:
        logging.error(f"❌ Error parsing NVD data: {e}")

def parse_data_to_database():
    # 1. First parse NVD data
    parse_NVD_data_to_database()

    # 2. THEN parse MITRE ATT&CK data
    parse_MITREATTACK_data_to_database()

def save_last_update_time():
    try:
        logging.info("Saving last update time...")
        ConnSQLite.save_last_update_time()
        logging.info("✅ Last update time saved successfully.")
    except Exception as e:
        logging.error(f"❌ Error saving last update time: {e}")
def get_last_update_time():
    try:
        logging.info("Getting last update time...")
        last_update_time = ConnSQLite.get_last_update_time()
        logging.info(f"✅ Last update time retrieved successfully: {last_update_time}")
        return last_update_time
    except Exception as e:
        logging.error(f"❌ Error getting last update time: {e}")
        return None

def parse_MITREATTACK_data_to_database():
    try:
        logging.info("🔵 Parsing MITRE ATT&CK data...")
        MITREATTACKAPI.insert_data_to_MITREATTACK_Tables()
        logging.info("✅ MITRE ATT&CK data parsed successfully.")
    except Exception as e:
        logging.error(f"❌ Error parsing MITRE ATT&CK data: {e}")
# 1. First create database
#create_database()

# 2. THEN parse data
parse_data_to_database()
