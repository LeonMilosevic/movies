FROM --platform=linux/amd64 python:3.9-slim-buster

WORKDIR /app

# Install OS dependencies
RUN apt-get update && apt-get install -qq -y \
    git gcc build-essential libpq-dev --fix-missing --no-install-recommends \
    && apt-get clean

# Make sure we are using latest pip
RUN pip install --upgrade pip

# Copy requirements.txt
COPY ./requirements.txt ./requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# copy rest of the code
COPY . .