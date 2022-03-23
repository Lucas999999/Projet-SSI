import os


class program:
    def __init__(self,name,desc,size,install,category,verif,dependances):
        self.name = name
        self.desc = desc
        self.size = size
        self.install = install
        self.category = category
        self.verif = verif
        self.dependences = dependances

    def  InstallFull(self):
        if(self.dependences != None):
            self.InstallDependances()
        self.Install()

    def InstallDependances(self):
        for dependance in self.dependences:
            print(dependance)

    def Install(self):
        for commande in self.install:
            errCode = os.system(commande)
            print(errCode)

