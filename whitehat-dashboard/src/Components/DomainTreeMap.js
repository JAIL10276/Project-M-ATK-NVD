import React from 'react';
import { Treemap, Tooltip, ResponsiveContainer } from 'recharts';

const sampleData = [
  { name: 'Windows', size: 400 },
  { name: 'Linux', size: 300 },
  { name: 'macOS', size: 300 },
  { name: 'IoT Devices', size: 200 },
  { name: 'Mobile', size: 100 },
];

const CustomizedContent = ({ depth, x, y, width, height, name }) => {
  return (
    <g>
      <rect
        x={x}
        y={y}
        width={width}
        height={height}
        style={{
          fill: depth < 2 ? '#8884d8' : '#83a6ed',
          stroke: '#fff',
          strokeWidth: 2,
        }}
      />
      {width > 60 && height > 20 && (
        <text x={x + 10} y={y + 20} fill="#fff" fontSize={12} fontWeight="bold">
          {name}
        </text>
      )}
    </g>
  );
};

const DomainTreemap = () => {
  return (
    <div className="p-4 shadow-xl rounded-2xl bg-white w-full h-[400px]">
      <h2 className="text-xl font-semibold mb-2">Vulnerabilities by Domain</h2>
      <ResponsiveContainer width="100%" height="100%">
        <Treemap
          width={400}
          height={200}
          data={sampleData}
          dataKey="size"
          aspectRatio={4 / 3}
          stroke="#fff"
          content={<CustomizedContent />}
        >
          <Tooltip />
        </Treemap>
      </ResponsiveContainer>
    </div>
  );
};

export default DomainTreemap;
