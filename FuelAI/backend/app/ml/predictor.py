import random

class DemandPredictor:
    def predict(self, current_inventory, recent_demand):

        avg = (
            sum(recent_demand) / len(recent_demand)
            if recent_demand else 1000
        )

        future_demand = avg * 1.2

        risk = "HIGH" if future_demand > current_inventory else "LOW"

        return {
            "predicted_demand": round(future_demand, 2),
            "risk": risk,
            "confidence": round(random.uniform(.80, .95), 2)
        }

predictor = DemandPredictor()
