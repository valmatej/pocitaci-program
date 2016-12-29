#!/usr/bin/python3.5

MUSIC_DIRECTORY = "/home/mates/Plocha/Valmatej/hudba/Music"



print(" ")
print("     Media player")
print("     version 1.0")
print("     by Tomáš Jirka and Matěj Valášek")
print(" ")
print("                MM      MM ")
print("                M M   M MM ")
print("                M  MMM   M ")
print("                M        M ")
print(" ")
print(" ")
print("              EEEEEEEEEEE")
print("              E")
print("              E ")
print("              EEEEEEEEEEE")
print("              E")
print("              E ")
print("              EEEEEEEEEEE ")
print(" ")
print("             DDDDD ")
print("             D    D")
print("             D     D")
print("             D      D ")
print("             D        D")
print("             D         D")
print("             D         D ")
print("             D        D ")
print("             D      D")
print("             D    D ")
print("             D  D")
print("             DDD")
print(" ")
print("           OOOO ")
print("           OOOO ")
print(" ")
print("           III")
print("           III")
print("           III")
print("           III")
print("           III")
print("           III")
print("      IIIIIIIIIIIII")
print(" ")
print("                 AAA ")
print("                A   A")
print("               A     A")
print("              A       A")
print("             A         A ")
print("            AAAAAAAAAAAAA  ")
print("           A             A ")
print("          A               A")
print("         A                 A")
print(" ")
print(" ")
print(" Pro vybrání jiného adresáře zadejte jinou cestu k adresáři,")
print("spuštěním zdrojového kódu a změňte cestu MUSIC_DIRECTORY")
print(" ")
print(" ")


from time import sleep
from os import listdir
from os.path import isfile, join
import subprocess


#funkce která vrátí seznam mp3 souborů z určitého adresáře
def get_files (directory):
    mp3_files = []
    for f in listdir(directory):
        if isfile(join(directory, f)) and f[-4:] == ".mp3":
            mp3_files.append(f)
    return sorted(mp3_files)

def zobrazeni_vyzvy(pocet_pisnicek):
    vyzva = "Choose the file you want to play:"
    while True:
        try:
            cislo_pisnicky = int(input(vyzva))
            if cislo_pisnicky > 0 and cislo_pisnicky <= pocet_pisnicek:
                break
        except:
            pass
        print("  It should be a number from 1 to", pocet_pisnicek)
    return cislo_pisnicky

mp3_files = get_files(MUSIC_DIRECTORY)

for i, f in enumerate(mp3_files, start=1):
    print(i,f)

cislo_vybrane_pisnicky = zobrazeni_vyzvy(len(mp3_files))
vybrany_soubor = mp3_files[cislo_vybrane_pisnicky -1]
print ("You chose a song number:", cislo_vybrane_pisnicky, vybrany_soubor)
print(" ")
print(" ")

subprocess.run(["mpg123", join(MUSIC_DIRECTORY, vybrany_soubor)])
while True:
    def zobrazeni_vyzvy(pocet_pisnicek):
        vyzva = "Choose the file you want to play:"
        while True:
            try:
                cislo_pisnicky = int(input(vyzva))
                if cislo_pisnicky > 0 and cislo_pisnicky <= pocet_pisnicek:
                    break
            except:
                pass
            print("  It should be a number from 1 to", pocet_pisnicek)
        return cislo_pisnicky


    mp3_files = get_files(MUSIC_DIRECTORY)

    for i, f in enumerate(mp3_files, start=1):
        print(i, f)

    cislo_vybrane_pisnicky = zobrazeni_vyzvy(len(mp3_files))
    vybrany_soubor = mp3_files[cislo_vybrane_pisnicky - 1]
    print("You chose a song number:", cislo_vybrane_pisnicky, vybrany_soubor)
    print(" ")
    print(" ")

    subprocess.run(["mpg123", join(MUSIC_DIRECTORY, vybrany_soubor)])

#sleep(3)












