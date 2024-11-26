
#lanceur de dés

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Zone des déclarations~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import random as nombre
import time
import json

liste = []
a = 0
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~zone création d'un JSON~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

fichier = "mes_des.json"

# Lecture du fichier JSON ou initialisation si vide
try:
    with open(fichier, 'r', encoding='utf-8') as f:
        donnees = json.load(f)
        liste = donnees.get("dés", [])  # Charger la liste des tâches
except FileNotFoundError:
    # Si le fichier n'existe pas, on initialise une structure par défaut
    donnees = {"dés": [6]}
    liste = donnees["dés"]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~zone des definitions des fonctions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def sauvegarder():
    """Sauvegarde les tâches dans le fichier JSON."""
    donnees["dés"] = liste  # Met à jour la clé "dés"
    with open(fichier, 'w', encoding='utf-8') as f:
        json.dump(donnees, f, ensure_ascii=False, indent=4)
    print("Vos modifications ont été sauvegardées.")

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
        print("le dé N°",a,"a",liste[a]," faces ")
        a += 1
    a = 0  
    time.sleep(2.5)

def ajouter_dés():
    nb_faces=int(input("veuillez choisir le nombre de faces de votre dés: "))
    if (nb_faces>0): #le 1 est accpecté car pourquoi pas ?
        liste.append(nb_faces)
        sauvegarder()
        time.sleep(1.5)
    else:
        print("veuillez entre un nombre supérieur à 0")
        time.sleep(1.5)
        ajouter_dés()

def supprimer_dés():
    visu_dés()
    nb_faces=int(input("veuillez choisir le nombre de faces de votre dés: "))
    liste.remove(nb_faces)
    sauvegarder()
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