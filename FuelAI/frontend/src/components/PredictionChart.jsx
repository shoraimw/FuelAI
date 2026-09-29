import {LineChart,Line,XAxis,YAxis,Tooltip,ResponsiveContainer} from "recharts";

const data=[
 {day:"Mon",fuel:400},
 {day:"Tue",fuel:520},
 {day:"Wed",fuel:450},
 {day:"Thu",fuel:700},
 {day:"Fri",fuel:620}
];

export default function PredictionChart(){
 return (
 <div className="card" style={{height:300}}>
 <h3>AI Fuel Demand Prediction</h3>
 <ResponsiveContainer>
 <LineChart data={data}>
 <XAxis dataKey="day"/>
 <YAxis/>
 <Tooltip/>
 <Line dataKey="fuel" strokeWidth={3}/>
 </LineChart>
 </ResponsiveContainer>
 </div>
 )
}