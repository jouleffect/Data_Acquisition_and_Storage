#!/bin/bash

echo "Elimino il container docker"
sleep 1
docker-compose down

echo "Elimino le immagini docker"
sleep 1
docker rmi postgres adminer
