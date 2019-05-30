
# -*- coding: utf-8 -*-



def NullKohad(poly):

    

    def f(xx1, poly):
        x = poly[0] + poly[1] * xx1
        for i in range(2,len(poly)):
            x = x + poly[i] * (xx1**i)
        return float(x)

    #arvutab Newton-Raphson'i meetodiga nullkohta kuni on saavutatud piisav tapsus
    def derit(min1,max1,tol,poly1,poly2,roots):
        x1 = min1+0.01
        x = 0
        part = 0.1
        while x1 < max1 and x1 > min1:
            x1 = x1 - f(x1,poly1)/f(x1,poly2)
            if abs(f(x1,poly1)) < tol*1e1:
                if round(x1,6) not in roots:
                    break
                else:
                    x1 -= part
                    part += 0.1
                    if part > 10:
                        break
        return round(x1,6)

    #sama asi, kuid vahe on selles, kuidas limiite kasitletakse; sellest oleneb loppvastus
    def derit2(min1,max1,tol,poly1,poly2,roots):
        x1 = max1
        x = 0
        part = 0.1
        while x1 > min1:
            x1 = x1 - f(x1,poly1)/f(x1,poly2)
            if abs(f(x1,poly1)) < tol*1e1:
                if round(x1,6) not in roots:
                    break
                else:
                    x1 -= part
                    part += 0.1
                    if part > 10:
                        break
        return round(x1,6)

    #...
    def minderit(min1,max1,tol,poly1,poly2,roots):
        x1 = max1
        x = 0
        part = 0.1
        while x1 > min1 and x1 < max1+0.01:
            x1 = x1 - f(x1,poly1)/f(x1,poly2)
            if abs(f(x1,poly1)) < tol:
                if round(x1,6) not in roots:
                    break
                else:
                    x1 += part
                    part += 0.1
                    if part > 10:
                        break
        return round(x1,6)

    #...
    def minderit2(min1,max1,tol,poly1,poly2,roots):
        x1 = min1
        x = 0
        part = 0.1
        while x1 < max1:
            x1 = x1 - f(x1,poly1)/f(x1,poly2)
            if abs(f(x1,poly1)) < tol*1e1:
                if round(x1,6) not in roots:
                    break
                else:
                    x1 += part
                    part += 0.1
                    if part > 10:
                        break
        return round(x1,6)


    #funktsioon, mis konverteerib funktsiooni Calculuse reeglite pohjal selle funktsiooni derivatiiviks
    def derconv(poly):
        del poly[0]
        for i in range(0,len(poly)):
            poly[i] = poly[i]*(i+1)
        return poly


    #algandmete sisetamine:
    x = poly

    #andmete analyys
    if "+" in x: #kui vorrandi leidub "+" mark
        x1 = x.split("+")
        for i in range(0,len(x1)):
            x2 = x1[i].split("-")
            x1[i] = x2[0]
            if len(x2) > 1:
                for k in range(1,len(x2)):
                    x1.append("-"+x2[k])
    else: #kui ei leidu "+" marki
        x1 = x.split("-")
        for i in range(0,len(x1)):
            for k in range(1,len(x)):
                if x1[i] in x[k:k+len(x1[i])]: #kui "-" märk sisaldub originaalsisendis olevas konkreetses muutujas
                    if "-" in x[k-1:k]:
                        x1[i] = "-" + x1[i] #lisab "-" märgi vajadusel
                        break


    #sisestatud vorrandi desifreerimine, ex., mis on ruutliige, lineaarliige, neljanda astme liige, etc...
    num = []        #list liikmete kordajate jaoks
    powers = []     #list liikmete tundmatute astendajate jaoks (0 tähendab vabaliiget)
    substring = ""  #abistringi tekitamine
    for i in range(0,len(x1)):
        substring = x1[i] #abistring, ei ole vajalik, kui teeb koodi lihtsamaks ja loetavamaks
        for k in range(0,len(substring)):
            if substring[k:k+2] == "**":
                
                powers.append(substring[k+2:len(substring)])
                num.append(substring[0:k].strip("x"))
                if num[len(num)-1].strip("-") == "": #kui kasutaja ei ole kordajat tundmatu ette kirjutanud, siis on kordaja 1
                    num[len(num)-1] = num[len(num)-1]+"1"
                substring = ""
                break
            
            elif substring[k:len(substring)] == "x":
                
                powers.append("1")
                num.append(substring[0:k])
                if num[len(num)-1].strip("-") == "": #kui kasutaja ei ole kordajat tundmatu ette kirjutanud, siis on kordaja 1
                    num[len(num)-1] = num[len(num)-1]+"1"
                substring = ""
                break
            
        if substring != "":
            powers.append("0")
            num.append(substring) #paneb katte saadud arvu listi


    #teeb stringid intideks
    powers = list(map(int, powers))

    #kui vabaliiget ei ole, siis lisab selle
    poly1 = []
    if 0 not in powers:
        powers.append(0)
        num.append("0")

    #arvude tegemine stringist floatideks
    num = list(map(float, num))

    #vorrandi koondamine (ex. x+x+x-x -> 2x)
    for n in range(0,2):
        for i in range(0,len(powers)):
            for k in range(i+1,len(powers)-1):
                if powers[i] == powers[k]:
                    num[i] += num[k]
                    del powers[k]
                    del num[k]

    #puuduvate liikmete lisamine (ex. ruutliige puudu. -> lisan 0x**2 vorrandisse)
    power2 = list(map(int, powers)) #selleks, et power2 oleks powers listist soltumatu
    power2.sort()
    k = 0
    for i in range(0,len(x1)): #selleks, et olla kindel, et koik puuduvad liikmed saavad taidetud
        s = len(powers)-1
        while k < s:
            if power2[k] + 1 != power2[k+1]:
                power2.insert(k+1,k+1)
                powers.append(k+1)
                num.append("0")
            k += 1

    #paneb tundmatute kordajad (k.a vabaliige) listi
    for i in range(0,len(powers)):
        for k in range(0,len(powers)):
            if powers[k] == i:
                poly1.append(float(num[k]))
                break

    #leiab suurima liikme kordajate seast
    largest = powers[0]
    for i in range(1,len(powers)): 
        if powers[i] > largest:
            largest = powers[i]

    #abimuutuja arvutamine, mis aitab satestada piire
    specialpart = 0.0
    for i in range(2,len(poly1)):
        if round(poly1[i]) != 0:
            specialpart = abs(poly1[i])**(1/(i**2))
            break

    #funktsiooni derivatiivi arvutamine
    poly2 = list(map(int,poly1))
    poly2 = derconv(poly2)


    #nullkohtade arvutamine
    roots1 = [] #teeb tyhja listi nullkohtade jaoks
    roots2 = []
    suurim1 = powers[0]
    for i in range(0,len(powers)):
        if powers[i] > suurim1:
            suurim1 = powers[i]

    if suurim1 < 3:
        roots1.append((-poly1[1]+(poly1[1]**2-4*poly1[0]*poly1[2])**0.5)/2.0)
        roots1.append((-poly1[1]-(poly1[1]**2-4*poly1[0]*poly1[2])**0.5)/2.0)
    else:
        min1 = -(abs(poly1[0])+len(poly1)**2) #votab voimalikult suure minimaalse vaartuse, kus nullkohad yldse paikneda saavad
        max1 =   abs(min1) #ning sama suure, kuid positiivse maksimaalse vaartuse

        roots1.append(    derit(min1,max1,1e-8,poly1,poly2,roots1)) #koikide funktsioonide vahe siin on suhtumine limiitidesse
        roots1.append( minderit(min1,max1,1e-8,poly1,poly2,roots1))
        roots1.append(minderit2(min1,max1,1e-8,poly1,poly2,roots1))
        roots1.append(   derit2(min1,max1,1e-8,poly1,poly2,roots1))

        for i in range(0,2*largest):
            min1 = roots1[i] + abs(roots1[i]/2)
            max1 = min1 + specialpart**2

            roots1.append(    derit(min1,max1,1e-8,poly1,poly2,roots1))
            roots1.append( minderit(min1,max1,1e-8,poly1,poly2,roots1))
            roots1.append(minderit2(min1,max1,1e-8,poly1,poly2,roots1))
            roots1.append(   derit2(min1,max1,1e-8,poly1,poly2,roots1))


        #sorteerimine ja yhesuguste liikmete eemaldamine
        roots1.sort()
        if len(roots1) > 1:
            i = 1
            while i < len(roots1):
                if roots1[i] == roots1[i-1]: #kui leidub yhesuguseid liikmeid
                    del roots1[i]
                else:
                    i += 1

        #kvaliteedikontroll
        i = 0
        while i < len(roots1):
            if abs(f(roots1[i],poly1)) > 1e-6: #eemaldab partsa, mis ei labi kvaliteedikontrolli
                del roots1[i]
            else:
                i+=1

    #nullkohtade valja printimine
    returnarray=[]
    for i in range(0,len(roots1)):
        returnarray.append(roots1[i])

    return returnarray

