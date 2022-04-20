class MenuComponent:
    def __init__(self,name,action,description):
        self.name = name
        self.action = action
        self.description = description

    def toString(self, lenMin, nbr):
        strRet = f"{self.name} {nbr}"
        while(len(strRet) < lenMin):
            strRet = strRet[0:len(self.name)] + " " + strRet[len(self.name):]
        return f"|{strRet}|"
    
    def execute(self):
        print(self.action(self.name))
        # self.action()