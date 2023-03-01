### MOVIES ###

This is a simple app to manage movies.

### HOW TO RUN ###
- build docker image database/Dockerfile 
  - will host postgres db in the container 
  - create tables on init
- build docker image movies/Dockerfile 
  - will host app and its scripts in the container
- run app/workflow.py
  - get data from local files
  - transform and validate data
  - truncate tables
  - insert to postgres container
  - truncate models tables
  - insert to models tables

If everything is fine, you should see the output of a query from movie reviewer.

### ISSUES that might occur ###
- ip address of postgres docker container might change, if so run:
  - docker inspect <container_id_of_postgres_docker> | grep IPAddress
  - update the ip address in utils/secrets/host