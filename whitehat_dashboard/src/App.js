import logo from './logo.svg';
import './App.css';
import CVSSCharts from './Components/CVSSCharts';
import CriticalVul from './Components/CriticalVul';
import RiskHeatMap from './Components/RiskHeatMap';
import VulTrend from './Components/VulTrend';
import DomainRiskTable from './Components/DomainRiskStatus';
import CIAImpact from './Components/CIAImpact';
import DynaAdvisory from './Components/DynaAdvisory';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>White Hat Cybersecurity Dashboard</h1>
        <div className='dashboard-container'>
          <CVSSCharts/>
          <CriticalVul />
          <RiskHeatMap/>
          <VulTrend/>
          <DomainRiskTable/>
          <CIAImpact/>
          <DynaAdvisory/>
        </div>
      </header>
    </div>
  );
}

export default App;
