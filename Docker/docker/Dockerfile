FROM postgres:latest

RUN apt-get update && apt-get install -y pgloader sqlite3

ENV POSTGRES_PASSWORD=password
ENV POSTGRES_USER=username
ENV POSTGRES_DB=database

COPY . .