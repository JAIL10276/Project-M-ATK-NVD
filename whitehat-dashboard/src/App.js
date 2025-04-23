import React from 'react';
import "./App.css";
import DomainSummary from "./Components/DomainSummary";
import VulnerabilityTable from "./Components/VulnerabilityTable";
import BLUFAdvisory from "./Components/BLUFAdvisory";
import SummaryCard from "./Components/SummaryCard";
import DashboardCharts from './Components/DashboardCharts';
import DomainTreemap from './Components/DomainTreeMap';
function App() {
  const data = {
    domain: "example.com",
    vulnerabilities: 5,
    threats: 3,
    lastScanned: "2023-10-01",
    vulnerabilitiesList: [
      { id: 1, type: "SQL Injection", severity: "High", status: "Open" },
      { id: 2, type: "Cross-Site Scripting", severity: "Medium", status: "Closed" },
      { id: 3, type: "Remote Code Execution", severity: "Critical", status: "Open" },
      { id: 4, type: "Denial of Service", severity: "Low", status: "Open" },
    ],
    blufAdvisory: {
      id: 12345,
      severity: "Critical",
      description: "SQL Injection vulnerability found in the login module.",
      recommendedAction: "Patch the application immediately.",
    },
  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>🛡️WhiteHat Dashboard🎯</h1>
        <div style = {{ display: "flex", flexwrap: "wrap", justifyContent: "center"}}>
          
            <div className='summary-card' style={{ display: 'flex', flexWrap: 'wrap', justifyContent: 'center' }}>
              
              <div className="summary-title" style={{ textAlign: 'center', marginBottom: '20px' }}>
                <h2 style={{maxHeight: '20px'}}>Domain Summary</h2>
                  <div className='summary-card-container'>
                    <DashboardCharts/>
                  </div>
                
              </div>
            </div>
        </div>
        <section>
          <h2>📜Domain Summary✏️</h2>
          <DomainSummary />
          
        </section>

        <section>
          <h2>👾Vulnerability & Threats❗</h2>
          <VulnerabilityTable />
        </section>

        <section>
          <h2>📃BLUF Advisory🔍</h2>
          <BLUFAdvisory />
        </section>
        <p>
          This dashboard provides a comprehensive overview of your domain's security status, including vulnerabilities, threats, and actionable insights.
        </p>



        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
