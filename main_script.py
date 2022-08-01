import base64
import string as chaine_de_characters
from sys import stdout as console
from os import get_terminal_size as savoir_la_taille_de_la_console
from time import sleep as dormir

chiffre = int
ecrire_dans_la_console = console.write
TEXTE_INUTILE:base64 = "RnJlbmNoIFByb2dyYW1tYXRpb24gW1RST0xMIENPREVd"

la_taille_de_la_console = savoir_la_taille_de_la_console()
le_nombre_de_repetition:chiffre = 0
Allumer = True

ATTENDRE:chiffre = ( 2 / 100 )


def Mettre_la_console_en_mode_ANSI():
    if __import__("platform").system() == "Windows":
        kernel32 = __import__("ctypes").windll.kernel32
        kernel32.SetConsoleMode( kernel32.GetStdHandle( -11 ), 7)
        del kernel32


def Si_la_console_change_de_taille(la_taille_de_la_console):
    return la_taille_de_la_console != savoir_la_taille_de_la_console()

def Savoir_si_la_console_change_de_taille(la_taille_de_la_console):
    if Si_la_console_change_de_taille(la_taille_de_la_console):
        return True
    return False


def si_le_texte_depasse_la_taille_de_la_console(la_taille_de_la_console_columns, le_nombre_de_repetition):
    return la_taille_de_la_console_columns <= le_nombre_de_repetition

def Savoir_si_le_texte_depasse_la_taille_de_la_console(la_taille_de_la_console_columns, le_nombre_de_repetition):
    if si_le_texte_depasse_la_taille_de_la_console(la_taille_de_la_console_columns, le_nombre_de_repetition):
        return True
    return False


Mettre_la_console_en_mode_ANSI()
while Allumer:
    if Savoir_si_la_console_change_de_taille(la_taille_de_la_console):
        la_taille_de_la_console = savoir_la_taille_de_la_console()
        console.write("\033[H\033[J\n") # Effacer la console

    if Savoir_si_le_texte_depasse_la_taille_de_la_console(la_taille_de_la_console.columns, le_nombre_de_repetition):
        exit()

    le_nombre_de_repetition += 1
    texte:chaine_de_characters = " "*le_nombre_de_repetition
    line:chiffre = (la_taille_de_la_console.lines // 2)
    column:chiffre = (la_taille_de_la_console.columns // 2) - (len( texte ) // 2)

    ecrire_dans_la_console(f"\x1B[{ line };{ column }H")
    ecrire_dans_la_console(f"\x1B[48;2;255;0;0m{ texte }\033[0m\n")

    dormir( ATTENDRE )