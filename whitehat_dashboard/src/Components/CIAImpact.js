import React from "react";
import Plot from "react-plotly.js"; 

function CIAImpact(){
    const labels = ['Confidentiality', 'Integrity', 'Availability'];
    const values = [40, 20, 24];

    return (
        <div className="Chart-Container">
            <h2>
                CIA Impact Distribution
            </h2>
            <Plot
                data = {[
                    {
                        labels: labels,
                        values: values,
                        type: 'pie',
                        hole: 0.7,
                        textinfo: 'label+percent',
                        textposition: 'outside',
                        marker: {
                            colors: ['#007bff', '#28a745', '#ffc107'],
                        },
                    },
                ]}
                layout={{
                    showlegend: true,
                    paper_bgcolor: '#282828',
                    plot_bgcolor: '#282828',
                    font: {color: '#f0f0f0'},
                }}
            />
        </div>
    );
}

export default CIAImpact;