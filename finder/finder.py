class finder:
    def __init__(self):
        self.ignore= {'kto', 'Kto'}

    def find(self,zdanie):
        self.dane=[]
        for s in zdanie.split():
            if s[0].isupper() and s not in self.ignore: self.dane.append(s)
        return self.dane
    
    def isIn(self, slowo):
        import os
        os.system("grep", slowo
