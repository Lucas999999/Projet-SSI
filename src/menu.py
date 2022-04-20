from .menuComponent import MenuComponent

class Menu:
    def __init__(self,name,components):
        self.name = name
        self.components = components

    # def componentToStringFormat(self, component, len)

    def toString(self):
        strRet = f"{self.name}"
        lenMax = len(self.name)

        for number, component in enumerate(self.components):
            if(lenMax< len(f"{component.name} {number}")):
                lenMax = len(f"{component.name} {number}")
        print(self.nameToString(lenMax))
        for number, component in enumerate(self.components):
            print(component.toString(lenMax, number))
        print(f"+{'-'*lenMax}+")

    def nameToString(self,lenMin):
        strRet = self.name
        compteur = 0
        while(len(strRet)<lenMin):
            if(compteur%2 == 1):
                strRet+="-"
            else:
                strRet = "-"+strRet
            compteur+=1
        return f"+{strRet}+"

    def execute(self):
        try:
            userChoice = int(input("que voulez vous faire ? :"))
        except:
            execute()
        self.execute(userChoice)

    def execute(self, userChoice):
        self.components[userChoice].execute()