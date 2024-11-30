#lanceur de dés

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Zone des déclarations~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import random as nombre
import time
import json
import os

liste = []
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~zone gestion JSON~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Définir le chemin du fichier .json dans le répertoire du projet
repertoire_du_projet = os.path.dirname(os.path.abspath(__file__))
fichier = os.path.join(repertoire_du_projet, "mes_des.json")

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
    for loop in range(len(liste)):
        résultat = nombre.randint(1, liste[loop])
        print(f"Le dé à {liste[loop]} faces est tombé sur le {résultat}.")
    time.sleep(2.5)

def visu_dés():
    for loop in range(len(liste)):
        print("le dé N°",loop+1,"a",liste[loop]," faces")
    time.sleep(2.5)

def ajouter_dés():
    try:
        nb_faces=int(input("Veuillez choisir le nombre de faces de votre dé :\n"))
        if (nb_faces>0): #le 1 est accpecté car pourquoi pas ?
            liste.append(nb_faces)
            sauvegarder()
            time.sleep(1.5)
        else:
            print("veuillez entre un nombre supérieur à 0")
            time.sleep(1.5)
            ajouter_dés()
    except ValueError:
        print("Valeur entré invalide")
        time.sleep(1.5)
        ajouter_dés()

def supprimer_dés():
    visu_dés()
    try:
        nb_faces=int(input("veuillez choisir le numéro de votre dés a supprimer: \n")) #on demande le numéro du dé a supprimer c'est plus simple que le nombre de face car sinon ca va pas supprimer le bon et c'est plus simple a comprendre
        liste.pop(nb_faces-1)
        sauvegarder()
        time.sleep(1.5)
    except ValueError:
        print("Valeur entrée invalide ou aucun dé trouvé. Veuillez entrer l'index du dé.")
        time.sleep(1.5)
        while True:
            try:
                nb_faces = int(input("veuillez choisir le nombre de faces de votre dés: \n"))
                liste.remove(nb_faces)
                sauvegarder()
                time.sleep(1.5)
                break
            except ValueError:
                print("Valeur entré invalide ou aucun dé trouvé")
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

    try : 
        choix=int(input("tapper 0, 1, 2 ou 3 selon votre choix :\n"))

        match choix: #remplace les if et elif par un match pour plus de lisibilité et une meilleur rapidité
            case 0 :
                print("arret du programme")
                exit()
            case 1 :
                print("vous avez choisi de lancer vos dés")
                lancement_dés()
            case 2 :
                print("vous avez choisi de visualiser vos dés")
                visu_dés()
            case 3 :
                print("vous avez choisi d'ajouter un dés")
                ajouter_dés()
            case 4 :
                print("vous avez choisi de supprimer un dés")
                supprimer_dés()
            case _ : #si le choix n'est pas dans les choix proposé
                print("veuillez tapper UNIQUEMENT 0, 1, 2, 3 ou 4 selon votre choix :\n")
                time.sleep(2)

    except ValueError:
        print("veuillez tapper UNIQUEMENT 0, 1, 2, 3 ou 4 selon votre choix :\n")
        time.sleep(2)
