FROM postgres:latest

# Set environment variables
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD postgres

# copy init.sql to create database and tables
COPY init.sql /docker-entrypoint-initdb.d/


