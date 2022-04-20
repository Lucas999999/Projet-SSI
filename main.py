import sys
from src.TextColor import TextColor
from src.menu import Menu
from src.testConnexion import testConnection
from src.arts import art
from src.programList import ProgramList
from src.verifRoot import VerifRoot
from src.menuComponent import MenuComponent
from src.menuList import MenuList
# from src.menu import Menu

def main():
    art.randomArt()
    if testConnection.checkConnection():
        print(f"{TextColor.CBOLD}{TextColor.CBLINK}{TextColor.CRED}[WARNING]{TextColor.CEND}{TextColor.CRED} fermeture du programme ...{TextColor.CEND}")
        sys.exit(1)
    if VerifRoot.testRoot():
        print(f"{TextColor.CBOLD}{TextColor.CBLINK}{TextColor.CRED}[WARNING]{TextColor.CEND}{TextColor.CRED} fermeture du programme ...{TextColor.CEND}")
        sys.exit(2)

def installs():
    for program in ProgramList.list:
        print(f"{program.category} --- {program.name}, {program.size}")

def test():
    MenuList.mainMenu.toString()
    MenuList.mainMenu.execute(-1)


main()
installs()
test()










# :alembic: