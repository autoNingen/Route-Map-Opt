project_name/
│
├── app.py                    # Entry point for the application
├── requirements.txt          # Dependencies
|
├── osrm_client.py            # Wrapper for interacting with OSRM
|
└── graphql_app/              # Directory containing all graphql logic
    ├── schema.py             # Define our types, queries etc.
    └── server.py             # Setup flask-graphql end-point

