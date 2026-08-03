# Route-Map-Opt
Route Map Optimizer utilizing GraphQL wrapper and OSRM API

project_name/
│
├── app.py                    # Entry point for the application
├── requirements.txt          # Dependencies
|
├── osrm_client.py            # Wrapper for interacting with OSRM
|
└── graphql_app/              # Directory containing all graphql logic
    ├── schema.py             # Define types, queries etc
    └── server.py             # Setup flask-graphql end-point
