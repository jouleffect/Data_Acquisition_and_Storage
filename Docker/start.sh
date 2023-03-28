#!/bin/bash

echo "Creo l'immagine e il container Docker"
sleep 1
docker-compose up -d --build

echo "Eseguo il dump del database"
sleep 3
docker exec -it postgres pgloader sqlite:///dati_generali.db pgsql://username@localhost/database
echo "Finito!"
echo ""
echo "#####################################"
echo "Link: http://localhost:8080/"
echo "Connessione: Sistema: PostgreSQL"
echo "Server: db"
echo "User: username"
echo "Password: password"
echo "Database: database"
echo "#####################################"