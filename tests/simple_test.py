from services.osrm_client import client

try:
    result = client.route([
        (7.41337, 43.72956), # start lon, lat
        (7.41546, 43.73077)
    ])
    print(result)
    
except Exception as e:
    print(f"Route could not be determined: {e}")

