import strawberry
from services.osrm_client import client

@strawberry.type
class Route:

    distance: float
    duration: float
    geometry: str

# creating a query

@strawberry.type
class Query:

    @strawberry.field
    def route(
        self,
        start_lon: float,
        start_lat: float,
        end_lon: float,
        end_lat: float,
    ) -> Route:

        result = client.route([
            (start_lon, start_lat),
            (end_lon, end_lat)
        ])

        route = result["routes"][0]

        return Route(
            distance=route["distance"],
            duration=route["duration"],
            geometry=route["geometry"],
        )