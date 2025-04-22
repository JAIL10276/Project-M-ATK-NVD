import json
import sqlite3

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
                        
                        for tactic in obj.get("kill_chain_phases", []):
                            kill_chain_name = tactic.get("kill_chain_name")
                            phase_name = tactic.get("phase_name")
                            cursor.execute('''
                                INSERT OR IGNORE INTO TechniqueKillChain (technique_ID, kill_chain_name, phase_name)
                                VALUES (?, ?, ?)
                            ''', (technique_id, kill_chain_name, phase_name))

                        for platform in obj.get("x_mitre_platforms", []):
                            cursor.execute('''
                                INSERT OR IGNORE INTO TechniquePlatforms (technique_ID, platform)
                                VALUES (?, ?)
                                ''',(technique_id, platform))
                        for permission in obj.get("x_mitre_permissions_required", []):
                            cursor.execute('''
                                INSERT OR IGNORE INTO TechniquePermissions (technique_ID, permissions)
                                VALUES (?, ?)
                                ''', (technique_id, permission))
                        for dataSource in obj.get("x_mitre_data_sources", []):
                            cursor.execute('''
                                INSERT OR IGNORE INTO TechniqueDataSources (technique_ID, dataSources)
                                VALUES (?, ?)
                                ''', (technique_id, dataSource))
                        for defense in obj.get("x_mitre_defense_bypassed", []):
                            cursor.execute('''
                                INSERT OR IGNORE INTO TechniqueDefensesBypassed (technique_ID, defense)
                                VALUES (?, ?)
                                ''', (technique_id, defense))
                        type_ = obj.get("type")
                        isRevoked = 1 if obj.get("revoked") else 0
                        isSubtechnique = 1 if obj.get("x_mitre_is_subtechnique") else 0
                        detection = obj.get("x_mitre_detection")
                        creationDate = obj.get("created")
                        modificationDate = obj.get("modified")
                        remote_support = obj.get("x_mitre_remote_support")
                        # Insert into Attack_technique
                        cursor.execute('''
                            INSERT OR IGNORE INTO Attack_technique (technique_ID, techniqueName, description, type, remoteSupport, isRevoked, isSubtechnique, detection, creationDate, modificationDate)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        ''', (technique_id, techniqueName, description, type_, remote_support, isRevoked, isSubtechnique, detection, creationDate, modificationDate))
                        # Insert DomainTechniqueMapping
                        for domain in obj.get("x_mitre_domains", []):
                            cursor.execute('''
                                INSERT OR IGNORE INTO DomainTechniqueMapping (technique_ID, domain_ID)
                                VALUES (?, ?)
                            ''', (technique_id, domain))

                        # Insert ExternalReferences
                        for reference in obj.get("external_references", []):
                            source = reference.get("source_name")
                            url = reference.get("url")
                            ref_description = reference.get("description")
                            external_id = reference.get("external_id")

                            cursor.execute('''
                                INSERT OR IGNORE INTO ExternalReferences (technique_ID, source, url, description)
                                VALUES (?, ?, ?, ?)
                            ''', (technique_id, source, url, ref_description))

                            if source and source.lower() == "cwe" and external_id:
                                cursor.execute('''
                                    INSERT OR IGNORE INTO TechniqueCWEMapping (technique_ID, CWE_ID)
                                    VALUES (?, ?)
                                ''', (technique_id, external_id))

                    # Insert TechniqueMitigationMapping
                    if obj.get("type") == "relationship" and obj.get("relationship_type") == "mitigates":
                        cursor.execute('''
                            INSERT OR IGNORE INTO TechniqueMitigationMapping (technique_ID, mitigation_ID)
                            VALUES (?, ?)
                        ''', (obj.get("source_ref"), obj.get("target_ref")))

            connection.commit()
            print("✅ MITRE ATT&CK data inserted successfully.")

    except sqlite3.OperationalError as e:
        print(f"SQLite error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()
