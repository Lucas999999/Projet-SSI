from msilib.schema import Component


class Menu:
    def __init__(self,name,components,exitMethod,returnMethod):
        self.name = name
        self.components = components

    def componentToStringFormat(self, component, len)

    def toString(self):
        strRet = f"---------------{self.name}---------------"
        compteur = 0

        for number, component in enumerate(self.components):
            compteur = number
            strRet+=
