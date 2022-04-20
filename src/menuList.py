from .menu import Menu
from .menuComponent import MenuComponent

class MenuList:
    def testMenu(testText):
        print(testText)

    mainMenu = Menu("MENU", [MenuComponent("Installer", print("a"), "Installations"),
    MenuComponent("Désinstaller", testMenu("b"), "Désinstallations"),
    MenuComponent("Vérifier", testMenu("c"), "Vérifications"),
    MenuComponent("Réparer", testMenu("d"), "Réparations"),
    MenuComponent("Quitter", testMenu("e"), "Quitter")])