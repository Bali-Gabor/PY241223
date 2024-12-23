# Írjunk programot, amelye véletlenszerűen generál 120 kockadobást, a számokat a képernyőre írja sorfolytonosan, majd 
# válaszol a következő kérdésekre:
# a. Melyik számot hányszor dobta a gép (mi a dobott számok gyakorisága)?
# b. Van-e olyan szám, amelynél a dobások száma pontosan az összdobások 1/6 része?
# c. Melyik számot dobta a gép legtöbbször? (Mi a dobássorozat módusza?)
# d. Melyik számot dobta a gép legkevesebbszer?
# e. Minden számot dobtunk legalább 15-ször?
# f. Van olyan a dobások közt, amikor egymás után ugyanazt dobta a gép

from moduls import *

kocka=dobas()
print(kocka)
darab=dobasok(kocka)

for index, szam in enumerate(darab): print(f'{index+1}: {szam} db')

print(keres(darab))
print(f'A legtövbbet dobott szám: {legtobb(darab)}')
print(f'A legkevesebbszer kidobott szám: {legkevesebb(darab)}')
print(legalabb(darab))
print(ugyanaz(kocka))