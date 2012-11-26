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
            self.city = base_form(self.city)

    # Jesli UpperCase przed w to jest to imie(nazwisko), inaczej po w ostatni upper to imie(nazwisko)
    def find(self):
        if " w " in self.zdanie: index = self.zdanie.find(" w ")
        elif " u " in self.zdanie: index = self.zdanie.find(" u ")
        elif " na " in self.zdanie: index = self.zdanie.find(" na ")
        citytmp = self.zdanie[index+2:] #zdanie po 'w'
        city = []
        for elem in citytmp.split():
            if elem[0].isupper(): # teraz jest tylko po w ale duze litery
                city.append(elem)
        city = ' '.join(city)
        self.place = city.split() #mozliwe miasta
        for s in self.zdanie[:index].split(): #czy jest przed w cos z duzej?
            if s[0].isupper() and s != "Kto": 
                self.name = s
        if not self.name: #jesli nie ma
            self.name = self.place[-1]
            self.place = self.place[:-1]
        self.city = " ".join(self.place)
        self.name = base_form(self.name)

