# https://sleyter.fr/projets.php

import requests

reponse = requests.get("https://sleyter.fr/projets.php")
if reponse.status_code == 200:
    reponse.encoding = "UTF-8"
    print(reponse.text)
else:
    print("ERREUR code : " +str(reponse.status_code))    