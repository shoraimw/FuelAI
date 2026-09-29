import Navbar from "../components/Navbar";
import StatCard from "../components/StatCard";
import PredictionChart from "../components/PredictionChart";
import RecommendationCard from "../components/RecommendationCard";

export default function Dashboard(){

return (
<>
<Navbar/>

<div style={{
padding:"30px",
display:"grid",
gap:"25px"
}}>

<div style={{
display:"grid",
gridTemplateColumns:"repeat(4,1fr)",
gap:"20px"
}}>
<StatCard title="Fuel Stock" value="8500 L"/>
<StatCard title="Predicted Demand" value="7200 L"/>
<StatCard title="Risk Level" value="Low"/>
<StatCard title="AI Status" value="Active"/>
</div>

<PredictionChart/>

<RecommendationCard/>

</div>
</>
)

}