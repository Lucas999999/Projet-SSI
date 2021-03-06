import os
from .TextColor import TextColor


class VerifRoot:

    def isRoot():
        userId = os.geteuid()
        return userId == 0

    def testRoot():
        print(f"{TextColor.CBOLD}{TextColor.CBLUE}[Test]{TextColor.CEND}{TextColor.CBLUE2} Test utilisateur {TextColor.CEND}")
        if VerifRoot.isRoot():
            print(f"{TextColor.CBOLD}{TextColor.CGREEN}[Test]{TextColor.CEND}{TextColor.CGREEN2} Vous êtes Root {TextColor.CEND}")
            return 0
        else:
            print(f"{TextColor.CBOLD}{TextColor.CBLINK}{TextColor.CRED}[WARNING]{TextColor.CEND}{TextColor.CRED} Vous n'exécutez pas le programme en tant que root (utilisez sudo){TextColor.CEND}")
            return 1

