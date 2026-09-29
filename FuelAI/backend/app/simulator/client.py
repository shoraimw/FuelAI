import requests
from app.config import SIMULATOR_URL

class SimulatorClient:
    def __init__(self):
        self.base_url = SIMULATOR_URL

    def get(self, endpoint):
        try:
            response = requests.get(
                self.base_url + endpoint,
                timeout=5
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": str(e)}

    def health(self):
        return self.get("/v1/health")

    def instance(self):
        return self.get("/v1/instance")

    def depots(self):
        return self.get("/v1/depots")

    def stations(self):
        return self.get("/v1/stations")

    def routes(self):
        return self.get("/v1/routes")

    def demand_history(self):
        return self.get("/v1/demand-history?limit=200")

    def metrics(self):
        return self.get("/v1/metrics")

simulator = SimulatorClient()
