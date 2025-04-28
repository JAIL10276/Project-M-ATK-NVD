import React from "react";
import Plot from "react-plotly.js";

function RiskHeatMap(){
    const domains = ['Supply Chain', 'Maritime', 'Security', 'Transportation'];
    const riskLevels = ['Low', 'Medium', 'High', 'Critical'];
     // Matrix of vulnerabilities (devices x risk levels)
    const riskMatrix = [
        [2, 3, 1, 0], // GPS Tracker
        [1, 4, 2, 1], // RFID Reader
        [0, 2, 3, 2], // Sensors
        [0, 1, 1, 3], // Cameras
  ];

  return (
    <div className="Chart-Container">
        <h2>Risk Heatmap by Domains</h2>
        <Plot
            data = {[
                {
                    z: riskMatrix,
                    x: riskLevels,
                    y: domains,
                    type: 'heatmap',
                    colorscale: [
                        [0.0, '#90ee90'],  // Light Green (Low)
                        [0.33, '#ffff00'], // Yellow (Medium)
                        [0.66, '#f08080'], // Light Red (High)
                        [1.0, '#000000'],  // Black (Critical)
                    ],
                    hoverongaps: false,
                },
            ]}
            layout={{
                title: 'Device Risk Heatmap',
                xaxis: {
                title: 'Risk Level',
                autorange: 'reversed',  // 👈 Flip right to left
            },
                yaxis: {
                    title: 'Device',
                },
                paper_bgcolor: '#282828',
                plot_bgcolor: '#282828',
                font: { color: '#f0f0f0' },
            }}/>
    </div>
        
  );
}

export default RiskHeatMap;