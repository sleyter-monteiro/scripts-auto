# Phoenix

import requests

reponse = requests.get("https://sleyter.net")
if reponse.status_code == 200:
    reponse.encoding = "UTF-8"
    print(reponse.text)
else:
    print("ERREUR code : " +str(reponse.status_code))    