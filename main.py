from src.testConnexion import testConnection
from src.arts import art
from src.programList import ProgramList
from src.verifRoot import VerifRoot
def main():
    art.randomArt()
    testConnection.checkConnection()
    VerifRoot.isRoot()
    menu = {"00":"full",
    "1":"basique",
    "2":"catégories",
    "3":"docker",
    "4":"update",
    "99":"exit"}
    print("  ========== Menu ==========")
    for action in menu:
        print(f"          {action} : {menu[action]}")

def installs():
    for program in ProgramList.list:
        print(f"{program.category} --- {program.name}, {program.size}")




main()
installs()
