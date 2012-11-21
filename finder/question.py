from .finder import base_form

class Question:
    """Potwierdza presupozycje pytania"""
    def __init__(self, zdanie = ""):
        self.zdanie = zdanie.replace("?","")
        self.name = ''
        self.place = []
        self.city = ''
        if zdanie:
            self.find()
            self.checker()

    # Jesli UpperCase przed w to jest to imie(nazwisko), inaczej po w ostatni upper to imie(nazwisko)
    def find(self):
        index = self.zdanie.find(" w ")
        city = self.zdanie[index+2:] #zdanie po 'w' 
        self.place = city.split() #mozliwe miasta
        for s in self.zdanie[:index].split(): #czy jest przed w cos z duzej?
            if s[0].isupper() and s != "Kto": 
                self.name = s
        if not self.name: #jesli nie ma
            self.name = self.place[-1]
            self.place = self.place[:-1]
        self.city = " ".join(self.place)
        self.name = base_form(self.name)


    def checker(self):
        directory = "./bazy/finbaza.fred1"
        found = False
        for line in open(directory):
            if not found and line.startswith(self.city):
                found = True
                self.city = line
        if not found:
            for line in open(directory):
                if not found and line.startswith(self.city[:-1]):
                    found = True
                    self.city = line
            if not found:
                for line in open(directory):
                    if not found and line.startswith(self.city[:-2]):
                        found = True
                        self.city = line
    

if __name__ == '__main__':
    x = Question("Kto zabil Kennedy'ego w Bydgoszczy")
    y = Question("Kto zabil w Dallas Kennedy'ego")
    z = Question("Kto zabil Flieger w New York")
