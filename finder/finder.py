class finder:
    """Potwierdza presupozycje pytania"""
    def __init__(self):
        self.name = ''
        self.place = []

    # Jesli UpperCase przed w to jest to imie(nazwisko), inaczej po w ostatni upper to imie(nazwisko)
    def find(self,zdanie):
        index = zdanie.find("w")
        city = zdanie[index+1:] #zdanie po 'w' 
        self.place = city.split() #mozliwe miasta
        for s in zdanie[:index].split(): #czy jest przed w cos z duzej?
            if s[0].isupper() and s != "Kto": 
                self.name = s
        if not self.name: #jesli nie ma
            self.name = self.place[-1]
            self.place = self.place[:-1]

    def checker(self):
        for line in open("../bazy/finbaza.fred"):
            if line.startswith(" ".join(self.place)):
                print(line)
        print(self.name, " ".join(self.place))


x = finder()
x.find("Kto zabil Kennediego w Dallas")
x.checker()
y = finder()
y.find("Kto zabil w Dallas Kennediego")
y.checker()
z = finder()
z.find("Kto zabil Fliegera w Santa Clara")
z.checker()
