import pandas as pd
import json
import sqlite3

# Leggo il file con i dati generali del lotto in un dataframe
data = pd.read_csv("Dati generali del lotto.csv",dtype=str)

# Leggo il file delle coordinate in un dataframe
coord = pd.read_csv("coordinate.csv",dtype=str)

# Concateno i dataframe in un unico dataframe
concat = pd.concat([data,coord], axis = 1)

# Salvo il dataframe su csv
concat.to_csv("Dati generali del lotto con coordinate.csv", index=False)

# Creo il database e mi connetto
conn = sqlite3.connect('dati_generali.db')
cursor = conn.cursor()

# Leggo il file csv che ho creato prima
full_data = pd.read_csv('Dati generali del lotto con coordinate.csv')

# Inserisco i dati del file nella tabella del db
full_data.to_sql('Dati_lotto', conn, if_exists='append', index = False)