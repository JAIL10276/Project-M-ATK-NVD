import React from "react";
import Plot from "react-plotly.js";

function VulTrend(){
    const months = ['January', 'February', 'March', 'April', 'May', 'June'];
    const vulnerabilities = [5, 8, 12, 7, 15, 18]; // run queries to extract entries for cves
    return(
        <div className="Chart-Container">
            <h2>Vulnerability Discovery Trend</h2>
            <Plot
                data = {[
                    {
                        x: months,
                        y: vulnerabilities,
                        type: 'scatter',
                        mode: 'lines+markers',
                        marker: {color: 'orange'},
                        line: { shape: 'spline', width: 3},
                        xaxis: {color: 'white' },
                        grid: {color: 'white'},
                        yaxis: {color: 'white'},

                    },
                ]}
                layout={{
                    title: 'New Vulnerabilities Over Time',
                    xaxis: {title: 'Month',  linewidth: 3},
                    yaxis: {title: 'Number ', linewidth: 3},
                    grid: {color: 'white'},
                    paper_bgcolor: '#282828',
                    plot_bgcolor: '#282828',
                    font: {color: '#f0f0f0'},
                    width: '100%',
                }}/>
        </div>
    );
}

export default VulTrend;