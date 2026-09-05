liste_vide = []
liste_nombre = [1, 2, 3, 4, 5]
liste_heterogene = [1, "deux", 3.0, True, None,35, [1, 2, 3], {"cle": "valeur"}]

# print(liste_nombre[3])  # Acceder au premier element de la liste
# print(liste_heterogene[-1])  # Acceder au dernier element de la liste
# print(liste_heterogene[6][1])  # Acceder au deuxieme element de la sous-liste
# print(liste_heterogene[7]["cle"])  # Acceder a la valeur de la cle dans le dictionnaire

# print("Longueur de la liste de nombres : ", len(liste_nombre))  # Obtenir la longueur de la liste
# print("Longueur de la liste heterogene : ", len(liste_heterogene))  # Obtenir la longueur de la liste
# print("Longueur de la sous-liste : ", len(liste_heterogene[6]))  # Obtenir la longueur de la sous-liste
# print("Longueur du dictionnaire : ", len(liste_heterogene[7]))  # Obtenir la longueur du dictionnaire

# Insertion d'un element
liste_nombre.append(6)  # Ajouter un element a la fin de la liste
liste_heterogene.insert(2, "trois")  # Inserer un element a une position specifique

# Suppression d'un element
del liste_nombre[2]  # Supprimer le troisieme element de la liste
del liste_vide  # Supprimer la liste vide
elt_deleted = liste_nombre.pop(1)  # Supprimer le deuxieme element de la liste et le stocker dans une variable
elt_deleted2 = liste_heterogene.remove("deux")  # Supprimer le premier element correspondant a la valeur specifiee
elt_deleted3 = liste_heterogene.pop()   # Supprimer le dernier element de la liste et le stocker dans une variable
# elt_deleted4 = liste_heterogene.clear()  # Supprimer tous les elements de la liste
elt_deleted5 = liste_nombre.pop(0)  # Supprimer le premier element de la liste et le stocker dans une variable

# Concat lestes
print("Liste de nombres 000 : ", liste_nombre)
full_liste = liste_nombre + liste_heterogene  # Concatener deux listes
# liste_nombre est passe par adresse
full_liste2 = liste_nombre
full_liste2.extend(liste_heterogene)  # Concatener deux listes et modifier la liste originale

# Sous liste
sub_liste = liste_heterogene[1:4]  # Obtenir une sous-liste de la liste heterogene de l'index 1 a l'index 4 (exclu)
sub_liste2 = liste_heterogene[:3]  # Obtenir une sous-liste de la liste heterogene du debut a l'index 3 (exclu)
sub_liste3 = liste_heterogene[3:]  # Obtenir une sous-liste de la liste heterogene de l'index 3 a la fin

# print("Liste vide : ", liste_vide)
print("Liste de nombres : ", liste_nombre)
print("Liste heterogene : ", liste_heterogene)
print("Liste concatenee : ", full_liste)
print("Liste concatenee 2 : ", full_liste2)
print("Sous-liste : ", sub_liste)
print("Sous-liste 2 : ", sub_liste2)
print("Sous-liste 3 : ", sub_liste3)
