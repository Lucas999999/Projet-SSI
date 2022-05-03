import os
from .TextColor import TextColor


class testConnection:
    def checkConnection():
        print(f"{TextColor.CBOLD}{TextColor.CBLUE}[Test]{TextColor.CEND}{TextColor.CBLUE2} Test de la connexion{TextColor.CEND}")
        errcode = os.system("ping 8.8.8.8 -c 4 > /dev/null 2>&1")
        if(errcode != 0):
            print(f"{TextColor.CBOLD}{TextColor.CBLINK}{TextColor.CRED}[WARNING]{TextColor.CEND}{TextColor.CRED} Il semblerait que vous ne soyez pas connecté à Internet{TextColor.CEND}")
            return 1
        errcode = os.system("ping google.com -c 1 > /dev/null 2>&1")
        if(errcode != 0):
            print(f"{TextColor.CBOLD}{TextColor.CBLINK}{TextColor.CRED}[WARNING]{TextColor.CEND}{TextColor.CRED} Il semblerait que vous n'ayez pas de résolution de noms{TextColor.CEND}")
            return 2
        print(f"{TextColor.CBOLD}{TextColor.CGREEN}[Test]{TextColor.CEND}{TextColor.CGREEN2} Vous êtes connecté {TextColor.CEND}")
        return 0
