from .program import program
#todo: ajouter dépendences
class ProgramList:
    def __init__(self):
        return

    def GetProgram(index):
        return list[index]

    def Install(self,index):
        # self.GetProgram(index).Install()
        print(self.GetProgram(index).toString())

    list = [program("nmap","mapping réseau","??",["apt-get install -y nmap"],"informations","nmap --version"),
    program("netdiscorver","mapping réseau","??",["apt-get install -y netdiscover"],"informations","netdiscover --version"),
    program("unix-privesc-check","recherche malconfigurations","??",["apt-get install -y unix-privesc-check"],"analyse vuln","??"),
    program("nikto","web server scanner","??",["apt-get install -y nikto"],"analyse vuln","??"),
    ## burpsuite docker ?
    program("sqlmap","mappage bdd","??",["apt update","apt install -y snapd","snap install core","snap install sqlmap"],"web-app","??"),
    program("wfuzz","fuzz payload","??",["pip install wfuzz"],"web-app","??"),
    program("SQLite database browser","edit database files","??",["snap install sqlitebrowser"],"evaluation database","??"),
    program("john","attaque mots de passe","??",["snap install john-the-ripper"],"attaque mot de passe","??"),
    program("medusa","password attack","??",["apt-get install -y medusa"],"attaque mot de passe","??"),
    program("wordlist","password attack","??",["apt install -y wordlists"],"attaque mot de passe","??"),
    program("hydra","password attack","??",["apt-get install hydra-gtk"],"attaque mot de passe","??"),
    program("hashcat","password attack","??",["apt-get install hashcat"],"attaque mot de passe","??"),
    program("patator","password attack","??",["apt-get -y install patator"],"attaque mot de passe","??"),
    program("spooftooph","bluetooth spoof","??",["apt install spooftooph"],"wireless attack","??")
    # aircrack-ng
    # kismet
    ## reverse enginerie
    # clang
    # radare2
    ## exploitation
    # metasploit
    # searchsploit
    ## sniff & sp
    # dnschef
    # netsniff-ng
    # rebind
    # macchanger
    # mitmproxy
    # wireshark
    ## maintien de l'accès
    # dbd
    # powersploit
    # sbd
    # weevely
    # laudanum
    # exe2hex
    # dns2tcp
    # iodine
    # pwnat
    # proxytunnel
    # mimikatz
    ## criminalistique
    # scalpel
    # pdfid
    # autopsy
    # binwalk
    # blkls
    # hashdeep
    # bulk_extractor
    ## rapports
    # faraday start
    # maltego
    # pipal
    ## social engineering
    # msf payload creator
    ## navigation web
    # tor 
    ]