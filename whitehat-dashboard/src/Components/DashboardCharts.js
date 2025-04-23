import React from "react";
import { Area, AreaChart, Bar, BarChart, Brush, CartesianAxis, CartesianGrid, Cell, ComposedChart, Cross, Curve, Customized, DefaultLegendContent, DefaultTooltipContent, Dot, ErrorBar, Funnel, FunnelChart, Global, Label, LabelList, Layer, Legend, Line, LineChart, Pie, PieChart, PolarAngleAxis, PolarGrid, PolarRadiusAxis, Polygon, Radar, RadarChart, RadialBar, RadialBarChart, Rectangle, ReferenceArea, ReferenceDot, ReferenceLine, ResponsiveContainer, Sankey, Scatter, ScatterChart, Sector, SunburstChart, Surface, Symbols, Text, Tooltip, Trapezoid, Treemap, XAxis, YAxis, ZAxis} from "recharts";
import GaugeChart from "react-gauge-chart";
const sampleLineData = [
    { name: 'Jan', vulnerabilities: 10 },
    { name: 'Feb', vulnerabilities: 15 },
    { name: 'Mar', vulnerabilities: 20 },
    { name: 'Apr', vulnerabilities: 25 },
  ];
  
  const sampleBarData = [
    { domain: 'Enterprise', threats: 35 },
    { domain: 'ICS', threats: 20 },
    { domain: 'Mobile', threats: 15 },
  ];
  
  const samplePieData = [
    { name: 'Low', value: 30 },
    { name: 'Medium', value: 45 },
    { name: 'High', value: 25 },
  ];

    const sampleGaugeData = [
        { name: 'Low', value: 30 },
        { name: 'Medium', value: 45 },
        { name: 'High', value: 25 },
    ];
  const COLORS = ['#00C49F', '#FFBB28', '#FF8042'];
  
  const DashboardCharts = () => {
    return (
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '2rem', padding: '2rem' }}>
        {/* Line Chart: CVEs over time */}
        <div className="dashboard-charts-container">
            <div className="chart-card">
            <h3  id="card-headers">Vulnerabilities Over Time</h3>
            <ResponsiveContainer width="100%" height="100%">
                <LineChart data={sampleLineData}>
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Line type="monotone" dataKey="vulnerabilities" stroke="#8884d8" strokeWidth={2} />
                </LineChart>
            </ResponsiveContainer>
            </div>

            {/* Bar Chart: Threats per Domain */}
            <div className="chart-card">
            <h3 id="card-headers">Threats Per Domain</h3>
            <ResponsiveContainer width="100%" height={300}>
                <BarChart data={sampleBarData}>
                <XAxis dataKey="domain" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Bar dataKey="threats" fill="#82ca9d" />
                </BarChart>
            </ResponsiveContainer>
            </div>

            {/* Pie Chart: Severity Distribution */}
            <div className="chart-card">
            <h3 id="card-headers">CVE Severity Distribution</h3>
            <ResponsiveContainer width="100%" height={300}>
                <PieChart>
                <Pie data={samplePieData} cx="50%" cy="50%" outerRadius={80} fill="#8884d8" dataKey="value" label>
                    {samplePieData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                    ))}
                </Pie>
                <Tooltip />
                <Legend />
                </PieChart>
            </ResponsiveContainer>
            </div>

            <div className="chart-card">
                <h3 id="card-headers">Threat Level</h3>
                <ResponsiveContainer width="100%" height={300} >
                    <GaugeChart id="gauge-chart" nrOfLevels={25} percent={0.6} arcWidth={0.15} needleColor="Red" colors={["#FF0000", "#00FF00"]} arcPadding={70} style={{ width: '100%', height: '100%' }} needleBaseColor="red"/>
                    
                </ResponsiveContainer>

            </div>
        </div>
    </div>
    
    );
  };
  
  export default DashboardCharts;