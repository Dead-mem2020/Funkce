def obvod(a):
    vysledek = 4*a
    return vysledek

def obsah(a):
    vysledek = a**2
    return vysledek

def objem_kvadru(a):
    vysledek = a**3
    return vysledek

#Přetypování a zadání
promena1 = int(input("Zadejte proměnou 1"))
print("Pro výpočet obvodu zadejte 1")
print("Pro výpočet obsahu zadejte 2")
print("Pro výpočet objemu zadejte 3")
#iluze volby uživatele
volba = input("Zadejte vaši volbu: ")

if volba == "1":
    vysledek = obvod(promena1)
    print("Výsledek je: ", vysledek)
elif volba == "2":
    vysledek = obsah(promena1)
    print("Výsledek je: ", vysledek)
elif volba == "3":
    vysledek = objem_kvadru(promena1)
    print("Výsledek je: ", vysledek)
else:
    print("AJ SI TY KOKO-")