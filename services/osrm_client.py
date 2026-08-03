import requests

OSRM_URL = "http://localhost:5000"

class OSRMClient:
    def route(self, coordinates):
        coord_string = ";".join(
            f"{lon},{lat}" for lon, lat in coordinates
        )

        response = requests.get(
            f"{OSRM_URL}/route/v1/driving/{coord_string}",
            params={
                "overview": "full",
                "geometries": "geojson",
                "steps": "true"
            }
        )

        response.raise_for_status()
        return response.json()

client = OSRMClient()