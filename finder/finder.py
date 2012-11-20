class finder:
    def __init__(self):
        self.dane=[]
        self.ignore={'Kto','kto'}
        self.place = ''

    def find(self,zdanie):
        import re
        for s in zdanie.split():
            if s[0].isupper() and s not in self.ignore: 
                self.dane.append(s)
                if re.match(".*w %s" % s, zdanie): self.place = s
#        return self.dane

    def checker(self):
        for line in open("../bazy/finbaza.fred"):
            for word in self.dane:
                if line.startswith(word):
                    print(line)
