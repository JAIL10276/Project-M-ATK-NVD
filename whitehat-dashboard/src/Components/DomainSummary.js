import React from "react";

const DomainSummary = () => {
  return (
    <div className="domain-summary">
      <h2>Domain Summary</h2>
      <table>
        <thead>
          <tr>
            <th>Domain</th>
            <th>Vulnerabilities</th>
            <th>Threats</th>
            <th>Last Scanned</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>example.com</td>
            <td>5</td>
            <td>3</td>
            <td>2023-10-01</td>
          </tr>
          <tr>
            <td>test.com</td>
            <td>2</td>
            <td>1</td>
            <td>2023-10-02</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
};

export default DomainSummary;