import React from 'react';
import Plot from 'react-plotly.js';

function CVSSCharts() {
  return (
    <div className='Chart-Container'>
      <h2>CVSS Score Distribution</h2>
      <Plot
        data={[
          {
            x: [5.3, 6.5, 7.8, 8.0, 9.0],
            type: 'histogram',
            marker: { color: '#28372' },
          },
        ]}
        layout={{
          
          title: 'CVSS Score Distribution across Domains',
          xaxis: { title: 'CVSS Score', color: 'white' },
          grid: {color: 'white'},
          yaxis: { title: 'Frequency', color: 'white'},
          paper_bgcolor: '#282828',
          plot_bgcolor: '#282828',
          font: {color: '#f0f0f0'},
          
        }}
      />
    </div>
  );
}

export default CVSSCharts;
