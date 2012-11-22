def podaj_zdania(text):
    text = text.replace("\n", "")
    return text.split(".")

def synonimy(slowo):
    ret = []
    stemp = base_form(slowo)
    with open("./bazy/dane.syn") as o:
        for linia in o:
            if stemp in linia:
                ret.append(linia)
    return ';'.join(ret).replace("\n", "").split(';')

def odmiany_synonimow(synlist):
    ret = []
    for elem in synlist:
        with open("./bazy/dane.odmian") as o:
            for linia in o:
                if elem in linia:
                    ret.append(linia)
    return ', '.join(ret).replace("\n", "").split(', ')

text = podaj_zdania(open("Kennedy.txt").read())
#text = podaj_zdania(open("narutowicz.txt").read())
#text = podaj_zdania(open("lennon.txt").read())

def znajdz_czas(text):
    ret = []
    with open("./bazy/zabil.all") as o:
        zabic = o.read().split("\n")[:-1]
    for elem in text:
        for slowo in zabic:
            if slowo in elem:
                ret.append((slowo, elem)) 
    return ret

def base_form(name):
    with open("./bazy/dane.odmian") as o:
        for line in o:
            if name in line:
                return line.split(', ')[0]
    return name

def potw_presup(name, miejsce, tekst):
    ifname = False
    ifplace = False
    for czas, line in tekst:
        if name in line:
            ifname = True
        if miejsce in line:
            ifplace = True
    if ifname and ifplace: return 3 #presupozycja potwierdzona
    elif ifname: return 2 
    elif ifplace: return 1
    else: return 0 #tekst nie zawiera dostatecznych informacji
    
def bloody_shot(zdania, osoba, miejsce):
    killer = []
    for elem in zdania:
        tmp = elem[1][elem[1].find(elem[0])+len(elem[0])+1:]
        for slowo in tmp.split():
            slowo = slowo.rstrip(',"')
            if slowo[0].isupper() and slowo not in osoba and slowo not in miejsce and 'przez' in elem[1]: killer.append(slowo)
    return killer

lol = 'Niedługo później policja schwytała Lee Harveya Oswalda, byłego żołnierza US Marines, znanego z marksistowskich sympatii.'
                        #Tego lol to trzeba potem wyperdolić

def whos_da_killa(killers, texters=[('jakis shit i tak nie znaczenia', lol)]):
    #killer = [base_form(elem) for elem in killers]
    import collections
    x = collections.Counter(killers)
    szuk =  x.most_common(1)[0][0]
    fullname = []
    index_upper = []
    for krotka in texters:
        zd = [slowo.rstrip(',').rstrip('.') for slowo in krotka[1].split()]
        print(zd)
        i_kill = zd.index(szuk)
        for i in zd:
            if i[0].isupper(): index_upper.append(zd.index(i))
        #index_upper=index_upper[::-1]
        import math
        for i in index_upper:
            if math.fabs(i-i_kill) <3 : #gimmi just a lil bit love
                fullname.append(zd[i])
    
    return ' '.join([base_form(elem) for elem in fullname])


def diffrenet_split(text):
    import re
    x = re.split("\s[a-z]*", text)
    for nr, elem in enumerate(x):
        if elem == "": 
            x[nr]='\n'
    return [elem.strip(" ") for elem in " ".join(x).split("\n")]
    

#czas = input("podaj czasownik: ")
if __name__ == '__main__':
    #print(base_form("Kennedy'ego"))
    #print(base_form("Piotrka"))
    #znajdz_czas()
    #print(potw_predy("Kennedy", "Dallas"))
    #print(znajdz_czas())
    #print(whos_da_killa(bloody_shot(znajdz_czas(), odmiany_synonimow(['Kennedy']), odmiany_synonimow(['Dallas']) )))
    print(bloody_shot(znajdz_czas(text), odmiany_synonimow(['Kennedy']), odmiany_synonimow(['Dallas'])))
    #czas = 'zabił'
    #with open("./bazy/zabil.all", "w") as o:
    #  for slowo in  odmiany_synonimow(synonimy(czas)):
    #       print(slowo, file=o)
#print(znajdz_czas(czas))
#print(podaj_zadania("Avdads.\nasdas asdkjsa.\n asdjkasdk.\n"))
#x = podaj_zadania(open("Kennedy.txt").read())
