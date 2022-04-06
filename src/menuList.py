from .menu import Menu
from .menuComponent import MenuComponent

class MenuList:
    mainMenu = Menu("MENU", [MenuComponent("Installer", print("a"), "Installations"), MenuComponent("Désinstaller", print("b"), "Désinstallations"), MenuComponent("Vérifier", print("c"), "Vérifications"), MenuComponent("Réparer", print("d"), "Réparations"), MenuComponent("Quitter", print("e"), "Quitter")])