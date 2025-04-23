import React from "react";

const SummaryCard = ({ title, value, icon }) => {
  return (
    <div className="summary-card">
      <div className="icon">{icon}</div>
      <h3>{title}</h3>
      <p>{value}</p>
    </div>
  );
}

export default SummaryCard;