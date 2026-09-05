import random

# 1. Choisir un nombre aleatoire entre 1 et 1000
nbr = random.randint(1, 1000)
nbr_entree = 0

# print("Random : ", nbr)

# while nbr_entree < 1 or nbr_entree > 1000:
#     print("Le nombre doit etre compris entre 0 et 1000.")
#     nbre_entree0 = input("Donnez un nombre entre 0 et 1000 : ")
# nbr_entree = int(nbre_entree0)

# 2. Tant que le nombre entre par l'utilisateur n'est pas egal au nombre mystere, demander a l'utilisateur de saisir un nouveau nombre
while nbr_entree != nbr:
    # 2.1. Demander a l'utilisateur de saisir un nombre entre 0 et 1000
    # Utilisez raw_input() pour récupérer en toute sécurité la saisie de texte dans Python 2.7
    nbr_entree0 = raw_input("Donnez un nombre entre 0 et 1000 : ")

    # Décoder la chaîne d'octets en un objet Unicode
    if not nbr_entree0.decode('utf-8').isnumeric():
        #if nbr_entree0 != "q":
        print("Veuillez entrer un nombre valide.")
        continue

    nbr_entree = int(nbr_entree0)
    # 2.2. Si le nombre entre est inferieur au nombre mystere, afficher "C'est plus grand que le random"
    if nbr_entree < nbr:
        print("C'est plus grand")
    # 2.3. Si le nombre entre est superieur au nombre mystere, afficher "C'est plus petit que le random"
    elif nbr_entree > nbr:
        print("C'est plus petit")
    # 2.4. Si le nombre entre est egal au nombre mystere, afficher "Felicitations ! Vous avez trouve le nombre mystere."
    else:
        print("Felicitations ! Vous avez trouve le nombre mystere.")