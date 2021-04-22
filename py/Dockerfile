FROM python:3.9.4-slim-buster

WORKDIR /pyserver

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
# RUN apt-get update \
#   && apt-get -y install netcat gcc \
#   && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . .