class Question:
    """Potwierdza presupozycje pytania"""
    def __init__(self):
        self.name = ''
        self.place = []
        self.city = ''

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
        self.city = " ".join(self.place)

    def checker(self):
        found = False
        for line in open("../bazy/finbaza.fred1"):
            if not found and line.startswith(self.city):
                found = True
                self.city = line
                print(line)
        if not found:
            for line in open("../bazy/finbaza.fred1"):
                if not found and line.startswith(self.city[:-1]):
                    found = True
                    print(line)
                    self.city = line
            if not found:
                for line in open("../bazy/finbaza.fred1"):
                    if not found and line.startswith(self.city[:-2]):
                        found = True
                        print(line)
                        self.city = line
        print(self.name, self.city)

if __name__ == '__main__':
    x = Question()
    x.find("Kto zabil Kennediego w Bydgoszczy")
    x.checker()
    y = Question()
    y.find("Kto zabil w Dallas Kennediego")
    y.checker()
    z = Question()
    z.find("Kto zabil Fliegera w New York")
    z.checker()
