def podaj_zdania(text):
    text = text.replace("\n", "")
    nowa = []
    pom = []
    for zdanie in text.split('.'):
        if zdanie:
            pom.append(zdanie)
            if not(zdanie[-1].isdigit() or zdanie[-1].isupper() or zdanie[-2:]=='ur' or zdanie[-2:]=='zm'):
                nowa.append("".join(pom))
                pom = []
    if pom: nowa.append("".join(pom))
    return nowa

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
    if ret: return ', '.join(ret).replace("\n", "").split(', ')
    else: return synlist

def znajdz_czas(text):
    ret = []
    with open("./bazy/zabil.all") as o:
        zabic = o.read().split("\n")[:-1]
    for elem in text:
        for slowo in zabic:
            if slowo in elem:
                ret.append((slowo, elem))
                break
    print("<br>Zdania, w których może być odpowiedź:<br><br>", bolder(ret),"<br>" + "*"*58 + "<br>" ,file=open('temp','a'))
    return ret

def bolder(krotka):
    ret = []
    for elem in krotka:
        p = []
        index = elem[1].find(elem[0])
        p+=elem[1][:index]
        p+='<b>'+elem[0]+'</b>'
        p+=elem[1][index+len(elem[0]):]
        ret.append(''.join(p))
    return ret

def base_form(name):
    with open("./bazy/dane.odmian") as o:
        for line in o:
            if name in line:
                return line.split(', ')[0].replace("\n","")
    return name

def potw_presup(name, miejsce, tekst):
    ifname = False
    ifplace = False
    #odmiany_miejsca = odmiany_synonimow([miejsce])
    for line in tekst.split('.'):
        if name in line:
            ifname = True
        for gdzie in miejsce:
            if gdzie in line:
                ifplace = True
    if ifname and ifplace: print('<font color="red"><b>Presupozycja potwierdzona:</b></font><br>Nazwisko %s oraz miejsce %s się zgadzają.' % (name, miejsce[0]), file=open('temp','a'));return 3 #presupozycja potwierdzona
    elif ifname: print('Nazwisko %s <b>potwierdzone</b>' % name, file=open('temp','a'));return 2
    elif ifplace: print('Miejsce %s <b>potwierdzone</b>' % miejsce[0], file=open('temp','a'));return 1
    else: print('Presupozycja <b>nie potwierdzona</b>', file=open('temp','a'));return 0#tekst nie zawiera dostatecznych informacji

def bloody_shot(zdania, osoba, miejsce):
    killer = []
    for elem in zdania:
        if 'postrzelił' in elem[1] and 'śmiertelnie' in elem[1]:
            tmp = elem[1]
        elif 'przez' in elem[1]:
            tmp = elem[1][elem[1].find(elem[0])+len(elem[0])+1:]
        elif 'zabił' in elem[1]:
            tmp = elem[1][:elem[1].find(elem[0])]
        else: continue
        for slowo in tmp.split():
            slowo = slowo.rstrip(',"')
            if not slowo: continue
            if slowo[0].isupper() and slowo not in osoba and slowo not in miejsce and base_form(slowo) not in open("./bazy/dane.miast").read().split("\n"):
                killer.append(slowo)
    #print(killer)
    return killer

def whos_da_killa(killers, texters, osoba, miejsce):
    import collections
    x = collections.Counter(killers)
    biggest = x.most_common()[0][1]
    szuk =  [os for os, liczba in x.most_common() if liczba == biggest]
    fullname = []
    index_upper = []
    for krotka in texters:
        zd = [slowo.rstrip(',.') for slowo in krotka[1].split()]
        for os in szuk:
            if os in zd:
                i_kill = zd.index(os)
                for i in zd:
                    if i[0].isupper(): index_upper.append(zd.index(i))
                for i in index_upper:
                    if abs(i-i_kill) <3 : #gimmi just a lil bit love
                        if zd[i] in fullname: continue
                        elif zd[i] not in osoba and zd[i] not in miejsce: fullname.append(zd[i])
                        else: fullname=[];break
            if fullname: break
    ret = ' '.join([base_form(elem) for elem in fullname])
    if ret: print('Nazwisko zabójcy', '<font color="red">'+ret+'</font>', file=open('temp','a'))
    #print(ret)
    return ret

