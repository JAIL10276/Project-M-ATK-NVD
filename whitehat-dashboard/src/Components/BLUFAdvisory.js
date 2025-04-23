import React from "react";

const BLUFAdvisory = () => {
    return (
        <div className="bluf-advisory">
        <h2>BLUF Advisory</h2>
        <p><strong>Bottom Line Up Front (BLUF):</strong></p>
        <p>Immediate action is required to address critical vulnerabilities in your system.</p>
        <p><strong>Details:</strong></p>
        <ul>
            <li>Vulnerability ID: 12345</li>
            <li>Severity: Critical</li>
            <li>Description: SQL Injection vulnerability found in the login module.</li>
            <li>Recommended Action: Patch the application immediately.</li>
        </ul>
        </div>
    );
    }
export default BLUFAdvisory;