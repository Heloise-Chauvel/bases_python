import numpy
import pandas
import requests
import json

url = "https://api.open-meteo.com/v1/forecast"

params_value ={
    "latitude": 48.8566,
    "longitude": 2.3522,
    "hourly": "temperature_2m",
    "timezone": "Europe/Paris"
}


reponse = requests.get(url, params=params_value)
if reponse.status_code ==200:
    donnees = reponse.json()
    #print(json.dumps(donnees))
else:
    print("Erreur dans la récupération de données.")
    exit()

hours = donnees['hourly']['time']
#print(hours)
#print(len(hours))
#print(hours[1])

heures = donnees['hourly']['time']
temperatures = donnees['hourly']['temperature_2m']
df = pandas.DataFrame({
    "Heure": heures,
    "Temp" : temperatures
})
#print(df.head(), "\n")
#print(df, "\n")
df_1 = df[df["Temp"] < 1.0]
df_aprem = df[(df["Heure"].dt is not None)&(df["Heure"].dt.hour) >= 12 & (df['Heure'].dt.hour <= 23)]
print(df_1, "\n")

#equivalent de classeur excel, permet de faire des calculs
numpy_temperatures = numpy.array(df_1['Temp'])

#print(temperatures)
#print(numpy_temperatures)

if len(numpy_temperatures) > 0:
    min_temp = numpy.min(numpy_temperatures)
    max_temp = numpy.max(numpy_temperatures)
    moy_temp = numpy.mean(numpy_temperatures)
    print(min_temp)
    print(max_temp)
    print(moy_temp)