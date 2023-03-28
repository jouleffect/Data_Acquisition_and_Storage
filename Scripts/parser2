from bs4 import BeautifulSoup
import os
import pandas as pd

# Percorso dove si trovano i dati
path = "htm/"
filelist = os.listdir(path)

# Inizializzo il dataframe
df = pd.DataFrame()

# Ciclo i file .htm
for i in filelist:
	if i.endswith(".htm"):
		with open(path + i, 'r') as file:
			rawdata = file.read()
			soup = BeautifulSoup(rawdata, 'html.parser')

			# Individuo il contenuto di interesse
			target = soup.find(lambda tag:tag.name=='div' 
							and 'card' in tag.get('class', '') 
							and 'Dati sulla procedura' in tag.text).find_all("span")

			# Creo il dizionario con i dati (chiave, valore), prendendo il testo per tag id e per class name
			data = {d.get('id'):str(d.text) for d in target if d.get('id')}
			class_target = {d.get('class')[0]:str(d.text) for d in target if d.get('class')}
			data.update(class_target)

			# Riempio il dataframe con i dati
			if df.columns.empty:
				df = pd.DataFrame(columns=data.keys())
				df.loc[len(df.index)] = list(data.values())
			else:
				df.loc[len(df.index)] = list(data.values())

# Salvo il dataframe su csv
df.to_csv("Dati sulla procedura.csv", index=False)
