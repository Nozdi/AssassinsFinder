class finder:
    def __init__(self):
        self.dane=[]
        self.ignore={'Kto','kto'}

    def find(self,zdanie):
        self.dane=[]
        for s in zdanie.split():
            if s[0].isupper() and s not in self.ignore: self.dane.append(s)
#        return self.dane

    def checker(self):
        for line in open("../bazy/finbaza.fred"):
            for word in self.dane:
                if line.startswith(word):
                    print(line)
