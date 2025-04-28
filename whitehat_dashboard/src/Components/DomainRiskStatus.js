import React from 'react';

function DomainRiskTable() {
  // Dummy domain risk data
  const domains = [
    { name: 'Transportation', vulnerabilities: 15, highestRisk: 'Critical' },
    { name: 'Security', vulnerabilities: 10, highestRisk: 'High' },
    { name: 'Maritime', vulnerabilities: 12, highestRisk: 'High' },
    { name: 'Supply Chain', vulnerabilities: 8, highestRisk: 'Medium' },
  ];

  return (
    <div className='Chart-Container'>
      <h2>Domain Risk Status</h2>
      <table className='Chart-Container' style={{ margin: '0 auto', borderCollapse: 'collapse', width: '80%' }}>
        <thead>
          <tr>
            <th style={headerStyle}>Domain</th>
            <th style={headerStyle}># Vulnerabilities</th>
            <th style={headerStyle}>Highest Risk</th>
          </tr>
        </thead>
        <tbody>
          {domains.map((domain, index) => (
            <tr key={index}>
              <td style={cellStyle}>{domain.name}</td>
              <td style={cellStyle}>{domain.vulnerabilities}</td>
              <td style={{ ...cellStyle, color: riskColor(domain.highestRisk) }}>{domain.highestRisk}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

// Simple table styling
const headerStyle = {
  border: '3px solid white',
  padding: '10px',
  backgroundColor: '#333',
  color: 'white',
  
};

const cellStyle = {
  border: '1px solid gray',
  padding: '10px',
  textAlign: 'center',
};

// Color code based on risk
function riskColor(riskLevel) {
  switch (riskLevel) {
    case 'Critical':
      return 'red';
    case 'High':
      return 'orange';
    case 'Medium':
      return 'yellow';
    case 'Low':
      return 'green';
    default:
      return 'white';
  }
}

export default DomainRiskTable;
