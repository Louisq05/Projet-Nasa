"""
Author : Louis QUIBEUF
Date : 14/03/2025
Context : Projet Nasa (météo, images ...)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

import requests
from PIL import Image
from io import BytesIO

# Récupération de la clé API NASA
KEY = ""

# Récupération de la météo sur Mars en format json
url_m = f"https://api.nasa.gov/insight_weather/?api_key={KEY}&feedtype=json&ver=1.0"
data_m = requests.get(url_m).json()

# Récupération de la photo du rover sur Mars 
url_p = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos?api_key={KEY}"
data_p = requests.get(url_p).json()

# Récupération du lien de l'image dans le json
hdurl = data_p["latest_photos"][12]["img_src"]

# Récupération de l'image sur internet avec le hdurl
response = requests.get(hdurl)
image = Image.open(BytesIO(response.content))
image.show()

"""
Résumé de la documentation de l'API Insight Mars Wheather Service
fournit les données météo suivantes (sur Mars) :
- Température           AT
- Pression atmo         PRE
- Vitesse du vent       HWS
- Direction du vent     WD

Ces données sont disponibles pour les 7 derniers sols (jours marsiens)
"""

sol_keys = data_m.get("sol_keys", []) # Liste des sols disponibles

if sol_keys :
    dernier_sol = sol_keys[-1] # on choisi le plus récent
    temperature = data_m.get(str(dernier_sol)).get("AT").get("av")
    print("Sur Mars, au jour",dernier_sol,"il faisait", temperature, "C°")

else :
    print("pas de données disponibles pour Mars.")