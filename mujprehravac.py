#!/usr/bin/python3.5

MUSIC_DIRECTORY = "/home/mates/Plocha/Valmatej/hudba/Music"

from os import listdir
from os.path import isfile, join
import subprocess
import time
#funkce která vrátí seznam mp3 souborů z určitého adresáře
while True:
    def get_files (directory):
        mp3_files = []
        for f in listdir(directory):
            if isfile(join(directory, f)) and f[-4:] == ".mp3":
                mp3_files.append(f)
        return sorted(mp3_files)

    while True:
        welcome_message1 = """

                               přehrávač mp3 souborů 'media'
                               aktuální verze 2.4
                               autoři: Tomáš Jirka a Matěj Valášek

                                                                    """

        print(welcome_message1)
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

        welcome_message = """ Pro vybrání jiného adresáře zadejte jinou cestu k adresáři
        spuštěním zdrojového kódu a změňte cestu MUSIC_DIRECTORY(druhá řádka v kódu)

        Novinky:

            !!!verze 1.0!!!

            -začátek vývoje!
            -pro přehrátí více písniček->nutnost pokaždé spouštět znovu
            -za dlouho, vytvoření místo jedné tři aplikace pro přehrátí mp3,mp4 a avi
            -anglicky některé pokyny
            ------------------------------------------------------------
            !!!verze 2.2!!!

            -opakování seznamu skladeb -> odpadá nutnost opakovaného
             spuštění souboru
            -a drobné změny v kódu
            -přidání více anglických a českých pokynů
            ------------------------------------------------------------
            !!!verze 2.3!!!

            -přidáno zobrazení aktuální cesty jak v 'aktuální cesta'
            -tak ve 'vybrali jste písničku číslo'
            -drobné úpravy v kódu.
            -vytvoření nápovědy pro plugin "mplayer" v angličtině
            -odkaz na stránky ke stažení a další text
            ------------------------------------------------------------
            !!!verze 2.4!!!

            -přepsání všech pokynů kompletně do češtiny
            -vytvoření kompletního seznamu novinek,který
             se snad bude dále doplňovat
            -drobné úpravy v kódu hlavně z hlediska přehlednosti kódu
            -nová odsazení textu
            -nová výzva k vybrání písně samozřejmě česky!
            -vytvoření hlášky "aktuální cesta"
            -doplnění "vybrali jste píseň číslo:" o zobrazení cesty
            ------------------------------------------------------------
            !!!verze 2.5!!!
            -oprava nesmyslů v textu
            -přidání dnešního dne a času spuštění programu
            -přidání hlášky pro stisknutí enteru
             kvůli možnému chybnému adresáři
             přidání upozornění na možné nefunkční funkce programu
             související s verzí Pythonu
            ------------------------------------------------------------

        veškeré chyby v textu,překlepy,upozornění,logo,přání posílejte
        na e-mail: valmatej@seznam.cz

        Více na www.linuxubuntu.estranky.cz v sekci přehrávač medií


                                                                             """
        print(welcome_message)
        print(" ")
        print(" ")
        print(" tato verze programu je vydána pro Python 3.5")
        print(" ")
        print(" upozornění!!: Některé funkce nemusí v jiných verzích pythonu fungovat!!!,např. funkce zobrazení datumu a času!!!")
        print(" ")
        print(" aktuální cesta-možno změnit v kódu(druhá řádka kódu) - ", MUSIC_DIRECTORY)
        print(" ")
        print(" ")
        print(" Dnes je:")
        print(time.strftime("%d/%m/%Y"))
        print(" ")
        print(" A program jste spustili v:")
        print(time.strftime("%H:%M:%S"))
        print(" ")
        print(" stiskněte klávesu enter pro pokračování a to proto,že ")
        print(" pokud jste zadali špatnou nebo žádnou cestu k adresáři,tak se aplikace po stisknutí enteru sama ukončí!!!) ")
        input()
        print(" ")
        print(" Načítání seznamu mp3 souborů:")
        print("        čekejte prosím...")
        print(" ")
        print(" ")
        def zobrazeni_vyzvy(pocet_pisnicek):
            print(" ")
            print(" Načítání seznamu mp3 souborů dokončeno!!")
            print(" ")
            print(" ")
            vyzva = "  vyberte soubor,který chcete spustit(napište číslo příslušné písně a zmáčkněte enter:"
            while True:
                try:
                    cislo_pisnicky = int(input(vyzva))
                    if cislo_pisnicky > 0 and cislo_pisnicky <= pocet_pisnicek:
                        break
                except:
                    pass
                print("  mělo to být číslo od 1 do", pocet_pisnicek)
            return cislo_pisnicky


        mp3_files = get_files(MUSIC_DIRECTORY)

        for i, f in enumerate(mp3_files, start=1):
            print(i, f)

        cislo_vybrane_pisnicky = zobrazeni_vyzvy(len(mp3_files))
        vybrany_soubor = mp3_files[cislo_vybrane_pisnicky - 1]
        print(" ")
        print(" ")
        print(" ")
        print(" vybral jste ve vybrané cestě písničku číslo: ", MUSIC_DIRECTORY, " - ", cislo_vybrane_pisnicky, vybrany_soubor )
        print(" ")
        print(" ")

        help = """ Nápověda:
        q-konec(quit)
        pravá a levá šipka určují pozici písně
        2x esc-druhá možnost konec(quit)
        mezerník-pauza písně



                                                """
        print(help)
        hlaskapredprehr =""" Pod tímto textem začíná samotný text a funkce přehrávače!

                                                                                        """
        print(hlaskapredprehr)
        subprocess.run(["mplayer", join(MUSIC_DIRECTORY, vybrany_soubor)])
        print(" ")
        print(" ")
        print(" ")













