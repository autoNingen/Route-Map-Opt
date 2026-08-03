Note: data must be prepared via OSRM extract, for example Monaco (~600kb)
use: 
wget https://download.geofabrik.de/europe/monaco-latest.osm.pbf

and extract routing graph:
docker run -t -v "${PWD}:/data" osrm/osrm-backend \
    osrm-extract -p /opt/car.lua /data/monaco-latest.osm.pbf
