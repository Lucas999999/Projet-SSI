import os


class VerifRoot:
    def isRoot():
        userId = os.geteuid()
        return userId == 0