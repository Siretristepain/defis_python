# On lis le contenu du fichier des noms
with open('liste_noms.txt', 'r') as f:
    contenu = f.readlines()

# On retire les caractères \n à la fin de chaque élément
contenu = [item.split("\n")[0] for item in contenu]

# On retire les éléments vides de la liste car le piège de l'exercice c'est qu'il y avait des lignes vierges au début et à la fin du fichier de noms
contenu = [item for item in contenu if item != ""]

# On initialise nos compteurs de nom avec/sans la lettre a
nb_noms_with_a = 0
nb_noms_without_a = 0

# On passe tous les noms en minuscules pour les problèmes de casse
for i in range(len(contenu)):
    contenu[i] = contenu[i].lower()

# On boucle sur tous les noms et on monitore la présence de la lettre a
for noms in contenu:
    if "a" in noms:
        nb_noms_with_a += 1

    elif "a" not in noms:
        #print(noms)
        nb_noms_without_a += 1


# On vérifie que la nombre cumulés de noms avec/sans la lettre a corresponde bien à la taille du contenu (c'est à dire au nombre de noms total) -> simple vérification inutile
if nb_noms_with_a + nb_noms_without_a != len(contenu):
    print(nb_noms_with_a + nb_noms_without_a)
    print(len(contenu))
    raise ValueError("La somme des noms trouvés ne corresponds pas au nombre de noms total.")


# Prints des résultats
print(f"Nb noms sans a : {nb_noms_without_a}.")

print(f"Il y a {len(contenu) - nb_noms_with_a} noms sans la lettre a.")
