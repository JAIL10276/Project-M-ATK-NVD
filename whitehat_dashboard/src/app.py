from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

MAIN_DATABASE = 'C:/Users/ayujo/SPRING2025/IST402/NVD_MTK/whitehat_dashboard/src/project-src/database/WHITEHAT.db'
SECOND_DATABASE = 'C:/Users/ayujo/SPRING2025/IST402/NVD_MTK/whitehat_dashboard/src/project-src/database/DomainAssetsVul.db'
import os
print(f"flask running on {os.getcwd()}")

@app.route('/project-src/database', methods=['GET'])
def getCVSSData():
    try:
        conn_wh = sqlite3.connect(MAIN_DATABASE)
        conn_da = sqlite3.connect(SECOND_DATABASE)
        cursor_wh = conn_wh.cursor()
        cursor_da = conn_da.cursor()
        conn_wh.row_factory= sqlite3.Row
        conn_da.row_factory= sqlite3.Row
        cursor_wh.execute(
            '''
                SELECT CVE_ID, confidentialityImpact, integrityImpact, availabilityImpact FROM CVSSData      
            '''
        )
        rows_wh = cursor_wh.fetchall()
        cursor_da = cursor_da.execute('SELECT "CVE ID", Domain, Description, CVSS, Advisory FROM AllDomains')
        rows_da = cursor_da.fetchall()

        cvss_data = []
        for row_wh,row_da in zip(rows_wh,rows_da):
            cvss_data.append({
                'CVE_ID': row_wh[0],
                'domain': row_da[1],
                'description': row_da[2],
                'CVSS': row_da[3],
                'Advisory': row_da[4],
                'confidentialityImpact': row_wh[1],
                'integrityImpact' : row_wh[2],
                'availabilityImpact': row_wh[3],
            })
        conn_wh.close()
        conn_da.close()
        return jsonify(cvss_data)
    
    except sqlite3.OperationalError as sq:
        print(sq)
        return jsonify({"error": str(sq)}), 500
    except Exception as e:
        print("🔥 ERROR CAUGHT:", e)
        return jsonify({"error": str(e)}), 500
    
    
if __name__ == '__main__':
    app.run(debug=True)