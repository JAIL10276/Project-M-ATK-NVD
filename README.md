# Project M-ATK-NVD

## 📑 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Database Structure](#-database-structure)
- [How to Run](#-how-to-run)
- [Repository Structure](#-repository-structure)
- [Notes](#-notes)
- [Future Improvements](#-future-improvements)
- [Disclaimer](#-disclaimer)
- [Author](#-author)

### 📚 Overview
**Project M-ATK-NVD** is a research-focused project that automates the extraction and mapping of cybersecurity vulnerabilities (CVEs) from the **NIST NVD API** and **MITRE ATT&CK framework** into a relational **SQLite database**.

The goal is to build a centralized, queryable structure for cybersecurity analysis, correlation between vulnerabilities and attack techniques, and support interactive visualizations (e.g., with Power BI).

---

### 🔧 Features
- 📥 **Automated Parsing** of NVD CVE data (with pagination and error handling)
- 📥 **Automated Parsing** of MITRE ATT&CK techniques, domains, mitigations, and external references
- 🔗 **Mapping of CVEs to CWEs** and CWEs to ATT&CK techniques
- 🛠️ **Database Creation**: Builds a relational SQLite database (`WHITEHAT.db`) with full foreign key constraints
- 🯩 **Support for platforms, permissions required, data sources, defenses bypassed, kill chain phases**, and more
- 📊 **Designed for integration into Power BI** and future dashboarding or querying projects

---

### 💂️ Database Structure
The database includes tables such as:
- **CVE**: Core vulnerability data
- **Metrics / CVSSData**: Severity scoring
- **Weaknesses**: CWE linkages
- **Configurations / CPEMatch**: Affected software/hardware configurations
- **SecurityControls**: References and remediations
- **Attack_technique**: MITRE techniques and metadata
- **Mappings**:
  - CVE ↔️ CWE
  - Technique ↔️ CWE
  - Technique ↔️ Platform
  - Technique ↔️ Permissions Required
  - Technique ↔️ Data Sources
  - Technique ↔️ Kill Chain Phases
- **Mitigations**: Recommended actions against techniques

---

### 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/JAIL10276/Project-M-ATK-NVD.git
   cd Project-M-ATK-NVD
   ```

2. Set up a virtual environment *(optional but recommended)*:
   ```bash
   python -m venv env
   source env/bin/activate   # (Linux/Mac)
   env\Scripts\activate      # (Windows)
   ```

3. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the parser:
   ```bash
   python Parser.py
   ```

5. Wait for all data to populate into `WHITEHAT.db`.

---

### 📄 Repository Structure
| File | Description |
|:----|:------------|
| `ConnSQLite.py` | Creates and structures the SQLite database |
| `NVDAPI.py` | Fetches and inserts NVD CVE vulnerability data |
| `MITREATTACKAPI.py` | Fetches and inserts MITRE ATT&CK data |
| `Parser.py` | Controls the full data pipeline from APIs to the database |

---

### ⚙️ Notes
- API rate limiting is handled with sleep timers and retry logic (NVD limits to ~5 requests/minute).
- MITRE ATT&CK data is processed from local JSON files (enterprise, ICS, and mobile attack data).
- Database schema is designed to normalize entries and allow flexible querying.
- CWE mappings are extracted from external references or weaknesses where available.

---

### 🔮 Future Improvements
- ✨ Add automated syncing with MITRE and NVD when new dumps are available.
- ✨ Build Power BI / dashboard templates directly from the database.
- ✨ Improve fault tolerance for rare API or data structure changes.

---

### 🛡️ Disclaimer
This project is intended for **educational and research purposes**.  
Always validate vulnerability information from official sources before making security decisions.

---

### 👨‍💻 Author
- GitHub: [JAIL10276](https://github.com/JAIL10276)

---

# 📊 Project M-ATK-NVD: Build Smarter, Safer Systems