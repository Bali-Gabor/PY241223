from random import randint


def dobas()->list[int]:
    kocka=[]
    for _ in range(120):
        kocka.append(randint(1,6))
    return kocka


def dobasok(lista:list)->list[int]:
    darab=[0, 0, 0, 0, 0, 0]
    for x in lista:
        match x:
            case 1: darab[0] = darab[0]+1
            case 2: darab[1] = darab[1]+1
            case 3: darab[2] = darab[2]+1
            case 4: darab[3] = darab[3]+1
            case 5: darab[4] = darab[4]+1
            case 6: darab[5] = darab[5]+1
    return darab


def keres(lista:list)->str:
    for szam in lista:
        if szam == 120 / 6:
            return 'Van oyan szám ami 20-szor lett kidobva.'
            break
    else: return 'Nincs olyan szám, ami 20-szor lett kidobva.'


def legtobb(lista:list)->int:
    index=0
    for x in range(1,len(lista)):
        if lista[index] < lista[x]: index=x
    return index+1


def legkevesebb(lista:list)->int:
    index=0
    for x in range(1, len(lista)):
        if lista[index] > lista[x]: index=x
    return index+1


def legalabb(lista:list)->str:
    index=0
    while index < len(lista) and lista[index] >= 15:
        index+=1
    if index < len(lista): return 'Nem lett minden szám 15-ször kidobva.'
    else: return 'Minden szám legalább 15-ször ki lett dobva.'


def ugyanaz(lista:list)->str:
    index=0
    while index < len(lista)-1 and lista[index] != lista[index+1]: index+=1
    if index < len(lista): return 'Lett ugyanaz a szám egymás után dobva.'
    else: return 'Nem lett ugyanaz a szám egymás után dobva.'

