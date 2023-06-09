# https://sleyter.fr/docs/Sleyter_MonteiroCV.pdf
# https://sleyter.fr/projet.php?id_projet=25

import requests

reponse = requests.get("https://sleyter.fr/projet.php?id_projet=25")
if reponse.status_code == 200:
    f = open("travaux.png", "wb")
    f.write(reponse.content)
    f.close()
    print("ecrite terminée")
    
else:
    print("ERREUR CODE : ", reponse.status_code)    