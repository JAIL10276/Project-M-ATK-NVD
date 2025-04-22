import NVDAPI
import MITREATTACKAPI
import ConnSQLite

def create_database():
    try:
        print("Creating database...")
        ConnSQLite.create_database()
        print("✅ Database and tables created successfully.")
    except Exception as e:
        print(f"❌ Error during database creation: {e}")
def parse_NVD_data_to_database():
    try:
        print("🔵 Parsing NVD data...")
        NVDAPI.insert_data_to_NVD_Tables()
        print("✅ NVD data parsed successfully.")
    except Exception as e:
        print(f"❌ Error parsing NVD data: {e}")

def parse_data_to_database():
    # 1. First parse NVD data
    parse_NVD_data_to_database()

    # 2. THEN parse MITRE ATT&CK data
    #parse_MITREATTACK_data_to_database()


def parse_MITREATTACK_data_to_database():
    try:
        print("🔵 Parsing MITRE ATT&CK data...")
        MITREATTACKAPI.insert_data_to_MITREATTACK_Tables()
        print("✅ MITRE ATT&CK data parsed successfully.")
    except Exception as e:
        print(f"❌ Error parsing MITRE ATT&CK data: {e}")
# 1. First create database
#create_database()

# 2. THEN parse data
parse_data_to_database()
