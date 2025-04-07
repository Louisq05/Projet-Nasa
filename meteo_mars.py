"""
Author : Louis QUIBEUF
Date : 14/03/2025
Context : Projet Nasa (météo, images ...)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

import requests
from PIL import Image
from io import BytesIO
from datetime import datetime, timedelta

# Récupération de la clé API NASA
KEY = ""

# Récupération de la météo sur Mars en format json
url_m = f"https://api.nasa.gov/insight_weather/?api_key={KEY}&feedtype=json&ver=1.0"
data_m = requests.get(url_m).json()

# Récupération de la photo du rover sur Mars 
url_p = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos?api_key={KEY}"
data_p = requests.get(url_p).json()
origine = datetime.strptime("2012-08-06", "%Y-%m-%d").date() # Jour du début de la misson (2012-08-06), format date 

nb_photos = len(data_p['latest_photos'])
date = earth_date = data_p['latest_photos'][0]['earth_date']

print(f"-----{nb_photos} available pitcures from Mars, {date}-----")
for i in range(nb_photos) :
    print(f"Picture n°{i} : ", end="")
    print(data_p['latest_photos'][i]['camera']['name'])

choice = int(input("Please choose a picture : n°"))


# Récupération du lien de l'image dans le json
hdurl = data_p["latest_photos"][choice]["img_src"]
date = data_p["latest_photos"][0]["earth_date"]
print(f"You choosed picture n°{choice} ({data_p['latest_photos'][choice]['camera']['name']}), from Mars {date}")
# Récupération de l'image sur internet avec le hdurl
response = requests.get(hdurl)
image = Image.open(BytesIO(response.content))
image.show()

