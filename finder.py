def podaj_zdania(text):
    text = text.replace("\n", "")
    return text.split(".")

import re

def odmiany(slowo):
    ret = ''
    with open("bazy/dane.odmian") as o:
        for linia in o.readlines():
            cos = linia.split(', ')
            if slowo in cos:
                return cos[0]

def synonimy(slowo):
    ret = []
    stemp = odmiany(slowo)
    for linia in open("bazy/dane.syn").readlines():
        if stemp in linia:
            ret.append(linia)
    return ';'.join(ret).replace("\n", "").split(';')

text=podaj_zdania(open("Kennedy.txt").read())

def odmiany_synonimow(synlist):
    ret = []
    for elem in synlist:
        with open("bazy/dane.odmian") as o:
            for linia in o.readlines():
                if elem in linia.split(', '):
                    ret.append(linia)
    return ', '.join(ret).replace("\n", "").split(', ')
                

def znajdz_czas(czas):
    ret = []
    ltemp = synonimy(czas)
    for slowo in ltemp:
        for elem in text:
            if slowo in elem:
                   ret.append(elem) 
    return ret


czas = input("podaj czasownik: ")
print(odmiany_synonimow(synonimy(czas)))
#print(znajdz_czas(czas))
#print(podaj_zadania("Avdads.\nasdas asdkjsa.\n asdjkasdk.\n"))
#x = podaj_zadania(open("Kennedy.txt").read())
