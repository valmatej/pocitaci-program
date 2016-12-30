#!/usr/bin/python3.5
from os import listdir, chdir
from os.path import isfile, join
import subprocess
import os, sys

MUSIC_DIRECTORY = "/home/mates/Plocha/Valmatej/hudba/Music"

welcome_message = """
     Media player
     version 2.0
     by Tomáš Jirka and Matěj Valášek

                MM      MM 
                M M   M MM 
                M  MMM   M 
                M        M 


              EEEEEEEEEEE
              E
              E 
              EEEEEEEEEEE
              E
              E 
              EEEEEEEEEEE 

             DDDDD 
             D    D
             D     D
             D      D 
             D        D
             D         D
             D         D 
             D        D 
             D      D
             D    D 
             D  D
             DDD

           OOOO 
           OOOO 

           III
           III
           III
           III
           III
           III
      IIIIIIIIIIIII

                 AAA 
                A   A
               A     A
              A       A
             A         A 
            AAAAAAAAAAAAA  
           A             A 
          A               A
         A                 A


 Pro vybrání jiného adresáře zadejte jinou cestu k adresáři,
spuštěním zdrojového kódu a změňte cestu MUSIC_DIRECTORY
"""


print(welcome_message)

# funkce která vrátí přejde do zadaného adresáře
def change_directory():
    soucasny_adresar = os.getcwd()
    novy_adresar = input("Zvolte adresář (" + soucasny_adresar + "): ")
    if novy_adresar == '':
        print("tak nic, zůstávám v", soucasny_adresar)
    else:
        try:
            chdir(novy_adresar)
        except Exception as e:
            print("Nelze přejít do adresáře " + novy_adresar, e)


#funkce která vrátí seznam mp3 souborů z určitého adresáře
while True:
    def get_files (directory):
        mp3_files = []
        for f in listdir(directory):
            if isfile(join(directory, f)) and f[-4:] == ".mp3":
                mp3_files.append(f)
        return sorted(mp3_files)

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


        change_directory()
        mp3_files = get_files(".")

        for i, f in enumerate(mp3_files, start=1):
            print(i, f)

        cislo_vybrane_pisnicky = zobrazeni_vyzvy(len(mp3_files))
        vybrany_soubor = mp3_files[cislo_vybrane_pisnicky - 1]
        print(" ")
        print("You chose a song number:", cislo_vybrane_pisnicky, vybrany_soubor)
        print(" ")
        print(" ")

        subprocess.run(["mpg123", join(MUSIC_DIRECTORY, vybrany_soubor)])


