#!/usr/bin/python3
from time import sleep
from random import randint

print(" Dobrý den,")
print(" ")
print(" ")
print(" já jsem počítací program,ve verzi 21.0")
print(" ")
print("    !!!Upozornění!!!")
print(" ")
print("    Již od verze 1.0 a verzích udělaných poté, je přísně zakázáno")
print(" ")
print(" používat kalkulačku jak hmotnou tak elektronickou na jakém-koli zařízení!!!,je pouze dovoleno používat")
print(" ")
print("    propisku a papír. ")
print(" ")
print(" ")


PLUS = '+'
MINUS = '-'
KRAT = '*'
DELENO = ':'
max_pocet = 10    # will be redefined by user

# funkce pro zobrazeni menu a ziskani pocetniho vykonu
def menu ():
    operatory = ['+', '-', '*', ':']

    vyzva = " vyberte si prosím početní výkon:"
    while True:
        try:
            i = int(input (vyzva + "\n"+
                " 1)+\n"+
                 " 2)-\n"+
                " 3)*\n"+
                " 4):\n"))
            if i in  [1,2,3,4]:
                break
        except:
            pass
        print(" mělo to být číslo od 1 do 4!")
        vyzva = " znovu si prosím vyberte početní výkon!:"

    print("Vybral jste:"+operatory[i - 1])
    return operatory[i - 1]

# funkce, ktera vygeneruje 2 nahodna cisla a vrati je
def vygeneruj_cisla(max_number=100):
    x = randint(1, max_number)
    y = randint(1, max_number)
    return x, y

# funkce, ktera vygeneruje 2 nahodna cisla, druhe mensi nebo rovno prvnímu číslu a vrati je
def vygeneruj_cisla_druhe_mensi(max_number=100):
    x = randint(1, max_number)
    y = randint(1, x)
    return x, y

# funkce, ktera spocita vysledek operace se 2 nahodnymi cisly
def spocitej(cislo1,operator,cislo2):
    if operator == PLUS:
        return cislo1 + cislo2
    elif operator == MINUS:
        return cislo1 - cislo2
    elif operator == KRAT:
        return cislo1 * cislo2
    elif operator == DELENO:
        return cislo1 / cislo2

# Zadej 1 priklad a opakuj, dokud to uzivatel nezodpovi spravne
def priklad(kolikaty, vsechny, operator, priklad_jednoduchy):
    if operator == DELENO:
        cislo1, cislo2 = vygeneruj_cisla(max_pocet)
        if cislo2 == 0:
            cislo2 = 20
        cislo1 = cislo1 * cislo2
    elif operator == MINUS:
        cislo1, cislo2 = vygeneruj_cisla_druhe_mensi(max_pocet)
    else:
        cislo1, cislo2 = vygeneruj_cisla(max_pocet)
    
    vysledekpc = spocitej(cislo1, operator, cislo2)

    while True:
        try:    
            vysledekuz = int(input(" spočítejte prosím tento příklad ("+
                str(kolikaty)+"/"+str(vsechny)+"): "
                + str(cislo1) + str(operator)+ str(cislo2)+"="))
            if vysledekuz==vysledekpc:
                print(" ")
                print(" tento výsledek je správně!!\n\n")
                break
            if priklad_jednoduchy:
                print("tento výsledek je špatně, ale to nevadí počítej dál")
                break
        except:
            print("  mělo to být číslo!")
            print(" tento výsledek je špatně!!")
        
def pocet_prikladu ():
    vyzva = "  zadejte prosím počet příkladů: "
    while True:
        try:
            pocet = int(input (vyzva))
            if pocet > 0 and pocet <= 100000000000000:
                break
        except:
            pass
        print("  mělo to být číslo,od 1 do 100")
    return pocet

def vyber_slozitosti():
    vyzva = """Vyberte si prosím jak složitý program chcete spustit:
    1) jednoduchý
    2) složitý\n"""
    while True:
        try:
            vyber = int(input (vyzva))
            if vyber >= 1 and vyber <= 2:
                break
        except:
            pass
        print("  mělo to být číslo,od 1 do 2")
    print("Vybral jste:", vyber)
    if vyber == 1:
        return 10, True
    else:
        return 100, False


max_pocet, priklad_jednoduchy = vyber_slozitosti()
pocet = pocet_prikladu()
operator = menu()
# Zadavej priklady
for i in range(pocet):
    priklad(i+1, pocet+1, operator, priklad_jednoduchy)
sleep(2)

    