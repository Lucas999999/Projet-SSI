from .menu import Menu
from .menuComponent import MenuComponent

class MenuList:
    def testMenu(testText):
        print(testText)

    mainMenu = Menu("MENU", [MenuComponent("Installer", testMenu, "Installations"),
    MenuComponent("Désinstaller", testMenu, "Désinstallations"),
    MenuComponent("Vérifier", testMenu, "Vérifications"),
    MenuComponent("Réparer", testMenu, "Réparations"),
    MenuComponent("Quitter", testMenu, "Quitter")])