import React from "react";
import Plot from "react-plotly.js";

function CriticalVul(){
    const cves = ['CVE-2023-1234', 'CVE-2022-5678', 'CVE-2021-9999', 'CVE-2024-1111', 'CVE-2020-4321'];
    const scores = [9.8, 9.7, 9.5, 9.3, 9.0];

    

    return (
        
        <div className="Chart-Container">
            <h2>Critical Vulnerabilities</h2>
            <Plot
                data={[
                    {
                        x: scores,
                        y: cves,
                        type: "bar",
                        orientation: 'h',
                        marker: {color: 'red'},
                    },
                ]}
                layout={
                    {
                        title: {title: 'Critical CVEs'},
                        xaxis: {title: 'CVE ID'},
                        paper_bgcolor: '#282828',
                        plot_bgcolor: '#282828',
                        font: {color: '#f0f0f0'},
                        xaxis: { title: 'CVSS Score', color: 'white' },
                        grid: {color: 'white'},
                        yaxis: { title: 'Frequency', color: 'white'},
                        
                    
                }}/>
        </div>
    );
}

export default CriticalVul;