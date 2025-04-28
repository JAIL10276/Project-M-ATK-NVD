import React from "react";

function DynaAdvisory(){
    // const | an array of items representing each domain its risk level 
    const domains = [
        { name: 'Transportation', risk: 'Critical', topCVE: 'CVE-2023-1234' },
        { name: 'Security', risk: 'High', topCVE: 'CVE-2022-5678' },
        { name: 'Maritime', risk: 'High', topCVE: 'CVE-2021-9999' },
        { name: 'Supply Chain', risk: 'Medium', topCVE: 'CVE-2020-4321' },
    ];

    return (
        <div style={advisoryContainer}>
            <h2>Threat Advisories</h2>
            {domains.map((domain,index)=> (
                <div key={index} style={advisoryCard}>
                    <h3>{domain.name} Domain</h3>
                    {generateAdvisory(domain)}
                </div>
            ))}
        </div>
    );
}

function generateAdvisory(domain){
    switch (domain.risk){
        case 'Critical':
            return `🚨Immediate action required: ${domain.name}`
        case 'High': 
            return `⚠️Elevated risk: ${domain.name}`
        case 'Medium':
            return `🔍 Moderate risk: ${domain.name}`
        case 'Low':
            return `❕Low risk: ${domain.name}`
        default:
            return `❔No specific advisory available for ${domain.name}`
    }
}
const advisoryCard = {
    backgroundColor: '#222',
    color: 'white',
    padding: '15px',
    margin: '10px 0',
    borderRadius: '8px',
    boxShadow: '0 0 10px rgba(255,0,0,0.3)',
    
  };
const advisoryContainer = {
    margin: '20px auto',
    padding: '20px',
    width: '90%',
}

export default DynaAdvisory;