def podaj_zdania(text):
    text = text.replace("\n", "")
    return text.split(".")

def odmiany(slowo):
    ret = ''
    with open("./bazy/dane.odmian") as o:
        for linia in o.readlines():
            cos = linia.split(', ')
            if slowo in cos:
                return cos[0]

def synonimy(slowo):
    ret = []
    stemp = odmiany(slowo)
    for linia in open("./bazy/dane.syn").readlines():
        if stemp in linia:
            ret.append(linia)
    return ';'.join(ret).replace("\n", "").split(';')

def odmiany_synonimow(synlist):
    ret = []
    for elem in synlist:
        with open("./bazy/dane.odmian") as o:
            for linia in o.readlines():
                if elem in linia.split(', '):
                    ret.append(linia)
    return ', '.join(ret).replace("\n", "").split(', ')

text = podaj_zdania(open("Kennedy.txt").read())
#text = podaj_zdania(open("narutowicz.txt").read())
#text = podaj_zdania(open("lennon.txt").read())
def znajdz_czas():
    ret = []
    with open("./bazy/zabil.all") as o:
        zabic = o.read().split("\n")[:-1]
    for elem in text:
        for slowo in zabic:
            if slowo in elem:
                ret.append((slowo, elem)) 
    return ret


#czas = input("podaj czasownik: ")
if __name__ == '__main__': 
    #znajdz_czas()
    print(znajdz_czas())
    #czas = 'zabił'
    #with open("./bazy/zabil.all", "w") as o:
    #  for slowo in  odmiany_synonimow(synonimy(czas)):
    #       print(slowo, file=o)
#print(znajdz_czas(czas))
#print(podaj_zadania("Avdads.\nasdas asdkjsa.\n asdjkasdk.\n"))
#x = podaj_zadania(open("Kennedy.txt").read())
