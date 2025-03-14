"""
Author : Louis QUIBEUF
Date : 13/03/2025
Context : Projet Nasa (météo, images ...)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

import requests


# Récupération de la clé API NASA  | link : https://api.nasa.gov/
KEY = "" 

# Récupération de la météo sur Mars en format json
url_m = f"https://api.nasa.gov/insight_weather/?api_key={KEY}&feedtype=json&ver=1.0"
data_m = requests.get(url_m).json()

"""
Résumé de la documentation de l'API Insight Mars Wheather Service
fournit les données météo suivantes (sur Mars) :
- Température           AT
- Pression atmo         PRE
- Vitesse du vent       HWS
- Direction du vent     WD

Ces données sont disponibles pour les 7 derniers sols (jours marsiens)
"""
temperature = data_m.get("675").get("AT").get("av")
print("Sur Mars, au jour 675 il faisait", temperature, "C°")




