class Menu:
    def __init__(self,name,components,exitMethod,returnMethod):
        self.name = name
        self.components = components

    # def componentToStringFormat(self, component, len)

    def toString(self):
        strRet = f"{self.name}"
        lenMax = 0
        compteur = 0

        for number, component in enumerate(self.components):
            compteur = number
            if(lenMax< len(f"{component.name} {number}")):
                lenMax = len(f"{component.name} {number}")

