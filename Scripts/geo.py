import pandas as pd
import requests
import json 

# Leggo il file in un dataframe
data = pd.read_csv("Dati generali del lotto.csv",dtype=str)

# Prelevo le colonne interessate
streets = data.indirizzo_lotto_pvp.values
caps = data.cap_zip_code_lotto_pvp
cities = data.citta_lotto_pvp
provinces = data.provincia_lotto_pvp
countries = data.nazione_lotto_pvp

lat = []
lon = []

# Ricerco le coordinate tramite le API di nominatim
for i in range(len(countries)):
    response = requests.get('https://nominatim.openstreetmap.org/search?format=json&street='+streets[i]
                            +'&county='+provinces[i]
                            +'&postalcode='+caps[i]
                            +'&country='+countries[i]
                            +'&addressdetails=1&limit=1')
    result = response.json()
    if not result:
        response = requests.get('https://nominatim.openstreetmap.org/search?format=json&&county='+provinces[i]
                            +'&postalcode='
                            +caps[i]
                            +'&country='
                            +countries[i]
                            +'&addressdetails=1&limit=1')
        result = response.json()
    
    for item in result:
        lat.append(item['lat'])
        lon.append(item['lon'])

# Salvo le coordinate in un dataframe
df = pd.DataFrame(data={'latitude': lat, 'longitude': lon})

# Salvo il dataframe su csv
df.to_csv("coordinate.csv", index=False)