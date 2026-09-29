class DecisionEngine:

    def generate(self, station, prediction):

        if prediction["risk"] == "HIGH":
            return {
                "action": "ALLOCATE_FUEL",
                "station": station,
                "quantity": prediction["predicted_demand"],
                "reason": [
                    "Demand increasing",
                    "Inventory shortage predicted"
                ]
            }

        return {
            "action": "NO_ACTION",
            "station": station,
            "reason": [
                "Inventory level acceptable"
            ]
        }

engine = DecisionEngine()
