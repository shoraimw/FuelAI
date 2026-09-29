const API="http://localhost:8000";

export async function getDashboard(){
 const res=await fetch(`${API}/dashboard`);
 return res.json();
}