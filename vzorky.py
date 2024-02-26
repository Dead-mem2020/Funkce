#Vytvářením funkcí začínáme slovem "def" (definujeme funkci) a následně název funkce
#V závorkách nalezneme paraetry funkce
#Parametryvoláme jako proměnou ve funkci, aniž bychom inicializovali proměnou 
#Pokud funkci zavoláme a zadáme její parametry, funkce je převezme 
def scitani(a, b):
    vysledek = a+b
    #Return je vrácení hodnoty z vyhodnocení funkce.Respektive nám vrací výsledek
    return vysledek

#Proměné které inicializujeme
#Defaultně se proměná ukládá v datovém typu string
promena1 = input("Zadejte proměnou 1")
promena2 = input("Zadejte proměnou 2")

promena1 = int(promena1)
promena2 = int(promena2)

vysledek = scitani(promena1, promena2)

print("Výsledek je: ",str(vysledek))
      #jde i ", vysledek)