FROM python:3.11.1-slim

MAINTAINER kaanozbudak
# pull the official docker image

# set work directory
WORKDIR /app

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY ./worker/ .