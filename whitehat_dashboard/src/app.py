from flask import Flask, jsonify, g
import sqlite3

app = Flask(__name__)

MAIN_DATABASE = './database/WHITEHAT.db'
SECOND_DATABASE = './database/DomainAssetsVul.db'
import os
print(f"flask running on {os.getcwd()}")



def getDataBase():
    database = getattr(g, '_database', None)

    if not database:
        conn = sqlite3.connect(MAIN_DATABASE)
        conn.row_factory = sqlite3.Row
        g._database = conn
    return g._database


@app.route('/project-src/database/CVSSData', methods=['GET'])
def getCVSSData():
    try:
    
        wdb= getDataBase()
        wdb.execute("ATTACH DATABASE 'DomainAssetsVul.db' AS domainDB")

        cursor = wdb.cursor()

        cursor.execute(
            f'''
                SELECT CVE.CVE_ID, Domain, domainDB.Description, CVSS, domainDBvisory FROM domainDB.AllDomains as domainDB
                JOIN CVE ON CVE.CVE_ID = domainDB.'CVE ID'
                WHERE CVE.CVE_ID = domainDB.'CVE ID'
            ''') 
        
        cursor.close()
        rows = cursor.fetchall()
        output = [dict(row) for row in rows]
        return output
    except sqlite3.OperationalError as sq:
        print(sq)
        return jsonify({"error": str(sq)}), 500
    except Exception as e:
        print("🔥 ERROR CAUGHT:", e)
        return jsonify({"error": str(e)}), 500

def getDomains():

    try:
    
        wdb= getDataBase()
        try:
            wdb.execute("ATTACH DATABASE 'DomainAssetsVul.db' AS domainDB")
        except Exception as e:
            print('Database alredomainDBy attached!')
        cursor = wdb.cursor()

        cursor.execute(
            f'''
                SELECT CVE.CVE_ID, Domain FROM domainDB.AllDomains as domainDB
                JOIN CVE ON CVE.CVE_ID = domainBD.'CVE ID'
                WHERE CVE.CVE_ID = domainDB.'CVE ID'
            ''') 
        
        
        rows = cursor.fetchall()
        cursor.close()
        output = [dict(row) for row in rows]
        return jsonify(output)
    except sqlite3.OperationalError as sq:
        print(sq)
        return jsonify({"error": str(sq)}), 500
    except Exception as e:
        print("🔥 ERROR CAUGHT:", e)
        return jsonify({"error": str(e)}), 500
@app.route('/project-src/database/CIA', methods=['GET'])
def getCIA():
     
    try:
        wdb= getDataBase()
        try:
            wdb.execute("ATTACH DATABASE 'DomainAssetsVul.db' AS domainDB")
        except Exception as e:
            print('Database alredomainDBy attached!')

        cursor = wdb.cursor()

        cursor.execute(
            f'''
                SELECT 
                    CVSSData.CVE_ID, 
                    Domain, CVSSData.confidentialityImpact, 
                    CVSSData.integrityImpact, 
                    CVSSData.availabilityImpact, 
                    CVSSData.accessVector, 
                    CVSSData.baseScore,  
                    Advisory FROM CVSSData                
                JOIN domainDB ON CVSSData.CVE_ID = domainDB.'CVE ID'
            ''') 
        
        cursor.close()
        rows = cursor.fetchall()
        output = [dict(row) for row in rows]
        return jsonify(output)
    except sqlite3.OperationalError as sq:
        print(sq)
        return jsonify({"error": str(sq)}), 500
    except Exception as e:
        print("🔥 ERROR CAUGHT:", e)
        return jsonify({"error": str(e)}), 500

    
if __name__ == '__main__':
    app.run(debug=True)
'''
 try:
        conn_wh = sqlite3.connect(MAIN_DATABASE)
        conn_da = sqlite3.connect(SECOND_DATABASE)
        cursor_wh = conn_wh.cursor()
        cursor_da = conn_da.cursor()
        conn_wh.row_factory= sqlite3.Row
        conn_da.row_factory= sqlite3.Row
        cursor_wh.execute(
          
                "SELECT CVE_ID, confidentialityImpact, integrityImpact, availabilityImpact FROM CVSSData"      
         
        )
        rows_wh = cursor_wh.fetchall()
        cursor_da = cursor_da.execute('SELECT "CVE ID", Domain, Description, CVSS, domainDBvisory FROM AllDomains')
        rows_da = cursor_da.fetchall()

        cvss_data = []
        for row_wh,row_da in zip(rows_wh,rows_da):
            cvss_data.append({
                'CVE_ID': row_wh[0],
                'domain': row_da[1],
                'description': row_da[2],
                'CVSS': row_da[3],
                'domainDBvisory': row_da[4],
                'confidentialityImpact': row_wh[1],
                'integrityImpact' : row_wh[2],
                'availabilityImpact': row_wh[3],
            })
'''