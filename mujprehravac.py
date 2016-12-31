#!/usr/bin/python3.5
from os import listdir, chdir
from os.path import isfile, join
import subprocess
import os, sys
import json

CONFIG_FILE = 'mujprehravac.json'
NIC_NEVYBRANO = -1
CHCI_SKONCIT = -2

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


"""


print(welcome_message)

# Funkce která přečte konfigurační soubor CONFIG_FILE ve formátu JSON, vrátí jeho obsah
def read_config():
    config_file_name = join(os.path.dirname(os.path.realpath(__file__)), CONFIG_FILE)
    with open(config_file_name) as cfg:
        config = json.load(cfg)
    return config



# Funkce která vrátí přejde do zadaného adresáře
def change_directory():
    soucasny_adresar = os.getcwd()
    novy_adresar = input("Zvolte adresář ('q' ukončení) [" + soucasny_adresar + "]: ")
    if novy_adresar == '':
        print("tak nic, zůstávám v", soucasny_adresar)
    elif novy_adresar == 'q':
        sys.exit(0)
    else:
        try:
            chdir(novy_adresar)
        except Exception as e:
            print("Nelze přejít do adresáře " + novy_adresar, e)


# Funkce která vrátí seznam mp3 souborů z určitého adresáře
def get_files (directory):
    mp3_files = []
    for f in listdir(directory):
        if isfile(join(directory, f)) and f[-4:] == ".mp3":
            mp3_files.append(f)
    return sorted(mp3_files)


# Funkce která se zeptá na soubor MP3 a vrátí jeho číslo
def zobrazeni_vyzvy(pocet_pisnicek):
    vyzva = "Choose the file you want to play ('q' to quit): "
    while True:
        try:
            odpoved = input(vyzva)
            if odpoved == '':
                return NIC_NEVYBRANO
            elif odpoved == 'q':
                return CHCI_SKONCIT
            cislo_pisnicky = int(odpoved)
            if cislo_pisnicky > 0 and cislo_pisnicky <= pocet_pisnicek:
                break
        except:
            pass
        print("  It should be a number from 1 to", pocet_pisnicek)
    return cislo_pisnicky



# Hlavní tělo programu
try:
    config = read_config()            # přečti config
    chdir(config['MUSIC_DIRECTORY'])  # přejdi do nakonfigurovaného adresáře
except Exception as e:
    print("Chyba:", e)


while True:
    change_directory()
    mp3_files = get_files(".")

    for i, f in enumerate(mp3_files, start=1):
        print(i, f)

    cislo_vybrane_pisnicky = zobrazeni_vyzvy(len(mp3_files))
    if cislo_vybrane_pisnicky == NIC_NEVYBRANO:
        continue
    elif cislo_vybrane_pisnicky == CHCI_SKONCIT:
        sys.exit(0)

    vybrany_soubor = mp3_files[cislo_vybrane_pisnicky - 1]
    print("\nYou chose a song number:", cislo_vybrane_pisnicky, vybrany_soubor, "\n")

    try:
        subprocess.run(["mpg123", vybrany_soubor])
    except KeyboardInterrupt:
        print("Přerušeno")


