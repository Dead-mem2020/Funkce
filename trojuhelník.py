#obvod a obsah
def obvod(a, b, c):
    vysledek = a+b+c
    return vysledek

def obsah(c, vc):
    vysledek = (c*vc)/2
    return vysledek

promena1 = int(input("Zadejte proměnou 1: "))
promena2 = int(input("Zadejte proměnou 2: "))
promena3 = int(input("Zadejte proměnou 3: "))
print("Pro obvod zadejte 1")
print("Pro obsah zadejte 2")
volba = input("Tak si vyber: ")

if volba == "1":
    vysledek = obvod(promena1, promena2, promena3)
    print("NO hurá,výsledek je ", vysledek)
elif volba == "2":
    vysledek = obsah(promena1, promena2)
    print("NO hurá,výsledek je ", vysledek)
else:
    ("Aj si ty žid?")