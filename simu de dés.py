
#lanceur de dés

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Zone des déclarations~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import random as nombre
import time

liste = [6]
a = 0

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~zone des definitions des fonctions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def lancement_dés():
    global a  
    for loop in range(len(liste)):
        résultat = nombre.randint(1, liste[a])
        print(f"Le dé à {liste[a]} faces est tombé sur le {résultat}.")
        a += 1
    a = 0  
    time.sleep(2.5)

def visu_dés():
    global a  
    for loop in range(len(liste)):
        print("le dé N°",a,"a ",liste[a]," faces ")
        a += 1
    a = 0  
    time.sleep(2.5)

def ajouter_dés():
    nb_faces=int(input("veuillez choisir le nombre de faces de votre dés: "))
    liste.append(nb_faces)
    time.sleep(1.5)


def supprimer_dés():
    nb_faces=int(input("veuillez choisir le nombre de faces de votre dés: "))
    liste.remove(nb_faces)
    time.sleep(1.5)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~le Main~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("bienvenue dans votre simulateur de dés")

while True:

    print("~~~~~~~~~~~~~~~~ menu: ~~~~~~~~~~~~~~~~~~")
    print("| tapper: 0 pour arreter le programme   |")
    print("| tapper: 1 lancer vos dés              |")
    print("| tapper: 2 visualiser vos dés          |")
    print("| tapper: 3 ajouter un dés              |")
    print("| tapper: 4 supprimer un dés            |")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    choix=int(input("tapper 0, 1, 2 ou 3 selon votre choix "))

    if choix==0:
        print("arret du programme")
        exit()
    elif choix==1:
        print("vous avez choisi de lancer vos dés")
        lancement_dés()
    elif choix==2:
        print("vous avez choisi de visualiser vos dés")
        visu_dés()
    elif choix==3:
        print("vous avez choisi d'ajouter un dés")
        ajouter_dés()
    elif choix==4:
        print("vous avez choisi de supprimer un dés")
        supprimer_dés()
    else:
        print("veuillez tapper UNIQUEMENT 0, 1, 2, 3 ou 4 selon votre choix ")
        time.sleep(2)