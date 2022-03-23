import sys
from src.TextColor import TextColor
from src.testConnexion import testConnection
from src.arts import art
from src.programList import ProgramList
from src.verifRoot import VerifRoot
# from src.menu import Menu

def main():
    art.randomArt()
    if testConnection.checkConnection():
        print(f"{TextColor.CBOLD}{TextColor.CBLINK}{TextColor.CRED}[WARNING]{TextColor.CEND}{TextColor.CRED} fermeture du programme ...{TextColor.CEND}")
        sys.exit(1)
    if VerifRoot.testRoot():
        print(f"{TextColor.CBOLD}{TextColor.CBLINK}{TextColor.CRED}[WARNING]{TextColor.CEND}{TextColor.CRED} fermeture du programme ...{TextColor.CEND}")
        sys.exit(2)
    print("  ========== Menu ==========")
    # for action in Menus.mainMenu:
    #     print(f"          {action} : {Menus.mainMenu[action]}")

def installs():
    for program in ProgramList.list:
        print(f"{program.category} --- {program.name}, {program.size}")

def test():
    listPrograms = ProgramList()
    testIndex = input("quel index à installer: ")
    listPrograms.Install(int(testIndex))


main()
installs()
test()










# :alembic: