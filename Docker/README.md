# Documentazione



#### Questa cartella contiene:

- La cartella ***docker*** con il **Dockerfile** e il database "***dati_generali.db***" creato dagli script.
- Il ***docker-compose.yml***, che configura i servizi di Postgres, con i parametri del database e l'interfaccia in ascolto sulla porta 8080.
- Lo script bash "***start.sh***", che avvia i Docker containers ed esegue il dump del file sqlite *dati_generali.db* nel db postgres. (Richiede permessi di esecuzione)
- Lo script bash "***stop.sh***", che arresta ed elimina i containers ed elimina le immagini Docker. (Richiede permessi di esecuzione)
- Questo file README.