import sqlite3
def create_database():
    try:
        with sqlite3.connect("WHITEHAT.db") as connection:
            print("✅ Connection to SQLite DB successful")
            print("🔃 Creating tables...")
            create_table(connection)
            connection.commit()
            print("✅ Database created successfully")
    except sqlite3.OperationalError as e:
        print(f"SQLite error: {e}")

def create_table(connection):
    cursor = connection.cursor()
    cursor.executescript('''
        -- CVE Core Table
        CREATE TABLE IF NOT EXISTS CVE (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            CVE_ID TEXT UNIQUE,
            sourceIdentifier TEXT,
            published TIMESTAMP,
            lastModified TIMESTAMP,
            vulnStatus TEXT,
            description TEXT
        );

        -- Metrics
        CREATE TABLE IF NOT EXISTS Metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            CVE_ID TEXT,
            source TEXT,
            type TEXT,
            CVSS_ID TEXT,
            baseSeverity TEXT,
            exploitabilityScore FLOAT,
            impactScore FLOAT,
            acInsufInfo INTEGER,
            obtainAllPrivilege INTEGER,
            obtainUserPrivilege INTEGER,
            obtainOtherPrivilege INTEGER,
            userInteractionRequired INTEGER,
            FOREIGN KEY (CVE_ID) REFERENCES CVE(CVE_ID)
        );

        -- CVSSData
        CREATE TABLE IF NOT EXISTS CVSSData (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            CVE_ID TEXT,
            CVSS_ID TEXT,
            version TEXT,
            vectorString TEXT,
            baseScore FLOAT,
            accessVector TEXT,
            accessComplexity TEXT,
            authentication TEXT,
            confidentialityImpact TEXT,
            integrityImpact TEXT,
            availabilityImpact TEXT,
            FOREIGN KEY (CVSS_ID) REFERENCES Metrics(CVSS_ID),
            FOREIGN KEY (CVE_ID) REFERENCES CVE(CVE_ID)
        );

        -- Weaknesses
        CREATE TABLE IF NOT EXISTS Weaknesses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            CVE_ID TEXT,
            source TEXT,
            type TEXT,
            CWE_ID TEXT,
            isClassified INTEGER,
            FOREIGN KEY (CVE_ID) REFERENCES CVE(CVE_ID),
            FOREIGN KEY (CWE_ID) REFERENCES CWE(CWE_ID)
        );

        -- CVETags
        CREATE TABLE IF NOT EXISTS CVETags (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            CVE_ID TEXT,
            Tags TEXT,
            FOREIGN KEY (CVE_ID) REFERENCES CVE(CVE_ID)
        );

        -- CPEMatch
        CREATE TABLE IF NOT EXISTS CPEMatch (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            CVE_ID TEXT,
            CPEMatch_ID TEXT,
            vulnerable INTEGER,
            criteria TEXT,
            matchCriteria_ID TEXT,
            FOREIGN KEY (CVE_ID) REFERENCES CVE(CVE_ID)
        );

        -- Configurations
        CREATE TABLE IF NOT EXISTS Configurations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            CVE_ID TEXT,
            operator TEXT,
            negate INTEGER,
            CPEMatch_ID TEXT,
            FOREIGN KEY (CVE_ID) REFERENCES CVE(CVE_ID),
            FOREIGN KEY (CPEMatch_ID) REFERENCES CPEMatch(CPEMatch_ID)
        );

        -- SecurityControls
        CREATE TABLE IF NOT EXISTS SecurityControls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            CVE_ID TEXT,
            url TEXT,
            source TEXT,
            FOREIGN KEY (CVE_ID) REFERENCES CVE(CVE_ID)
        );

        -- Attack Technique
        CREATE TABLE IF NOT EXISTS Attack_technique (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            technique_ID TEXT,
            techniqueName TEXT,
            description TEXT,
            type TEXT,
            remoteSupport INTEGER,
            isRevoked INTEGER,
            isSubtechnique INTEGER,
            detection TEXT,
            creationDate TIMESTAMP,
            modificationDate TIMESTAMP
        );
        
        -- DomainTechniqueMapping
        CREATE TABLE IF NOT EXISTS DomainTechniqueMapping (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            technique_ID TEXT,
            domain_ID TEXT,
            FOREIGN KEY (technique_ID) REFERENCES Attack_technique(technique_ID)
        );

        -- ExternalReferences
        CREATE TABLE IF NOT EXISTS ExternalReferences (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            technique_ID TEXT,
            source TEXT,
            url TEXT,
            description TEXT,
            FOREIGN KEY (technique_ID) REFERENCES Attack_technique(technique_ID)
        );

        -- TechniqueCWEMapping
        CREATE TABLE IF NOT EXISTS TechniqueCWEMapping (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            technique_ID TEXT,
            CWE_ID TEXT,
            FOREIGN KEY (technique_ID) REFERENCES Attack_technique(technique_ID),
            FOREIGN KEY (CWE_ID) REFERENCES CWE(CWE_ID)
        );

        -- CWE
        CREATE TABLE IF NOT EXISTS CWE (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            domain TEXT,
            CWE_ID TEXT
        );

        -- TechniqueMitigationMapping
        CREATE TABLE IF NOT EXISTS TechniqueMitigationMapping (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            technique_ID TEXT,
            mitigation_ID TEXT,
            FOREIGN KEY (technique_ID) REFERENCES Attack_technique(technique_ID)
        );

        -- CVE to CWE Mapping
        CREATE TABLE IF NOT EXISTS CVE_CWE_Mapping (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            CVE_ID TEXT,
            CWE_ID TEXT,
            FOREIGN KEY (CVE_ID) REFERENCES CVE(CVE_ID),
            FOREIGN KEY (CWE_ID) REFERENCES CWE(CWE_ID)
        );
        CREATE TABLE IF NOT EXISTS TechniquePlatforms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            technique_ID TEXT,
            platform TEXT,
            FOREIGN KEY (technique_ID) REFERENCES Attack_technique(technique_ID)
        );
        CREATE TABLE IF NOT EXISTS TechniquePermissions(           
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            technique_ID TEXT,
            permissions TEXT,
            FOREIGN KEY (technique_ID) REFERENCES Attack_technique(technique_ID)
        );
        CREATE TABLE IF NOT EXISTS TechniqueDataSources(          
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            technique_ID TEXT,
            dataSources TEXT,
            FOREIGN KEY (technique_ID) REFERENCES Attack_technique(technique_ID)
        );
        CREATE TABLE IF NOT EXISTS TechniqueDefensesBypassed(            
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            technique_ID TEXT,
            defense TEXT,
            FOREIGN KEY (technique_ID) REFERENCES Attack_technique(technique_ID)
        );
        CREATE TABLE IF NOT EXISTS TechniqueKillChain (            
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            technique_ID TEXT,
            kill_chain_name TEXT,
            phase_name TEXT,
            FOREIGN KEY (technique_ID) REFERENCES Attack_technique(technique_ID)
        );
    ''')
    print("✅ Tables created successfully!")