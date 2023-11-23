# This repo is testing the data lake house in local machine
- source: https://github.com/delta-io/delta-docker
- Build the docker and Run the docker compose
- Create a required folder for delta testing 
# create a volume mount file path 
- mkdir -p data/ logs/ delta/ notebooks/ resources/ src/ configs/
- mkdir -p delta/archive delta/tables delta/timeseries

# Take the risk [Don't run in Production server]
- sudo chmod -R 777 src/
- sudo chmod -R 777 data/
- sudo chmod -R 777 logs/
- sudo chmod -R 777 delta/
- sudo chmod -R 777 notebooks/
- sudo chmod -R 777 resources/

# Run the docker image 
- docker-compose up -d 

# to get token 
- docker ps 
- docker exec -it <dockerid> /bin/bash
- jupyter server list

# open the browser 
- http://localhost:8888 
- add the pySpark Notebook in notebooks
