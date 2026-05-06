import re

# =================
# Ouvrir le fichier
# =================

""" 
Ici, on ne veut pas séparer chaque ligne du fichier d'entrée.
En effet, les lignes fonctionnent par 2, la première concerne le GET et donne la position du caractère, et la seconde donne la réponse avec le caractère.
On veut donc split le fichier par "groupe" de 2 lignes.
On voit que chaque "groupe" est séparer par un saut de ligne (-> plus précisément par une ligne vide).
Cela corresponds à un double saut de ligne (donc \n\n).

On esquive aussi le dernier élément car la fin du fichier contient une double ligne vide, donc on récupère un élément vide sinon.
(une autre alternative plus simple serait de retirer les 2 lignes vides de la fin du fichier, mais je tiens à ne pas altérer du tout le fichier d'input).
"""
with open("sur_ecoute/src/message.txt", "r") as f:
    content = [bloc for bloc in f.read().split('\n\n')[:-1]]

# ===============
# Tri des groupes
# ===============

tuples = []

for groupe in content:
    line_1 = groupe.split('\n')[0]
    line_2 = groupe.split('\n')[1]

    # On utilise un lookbehind pour capturer tous les digits qui suivent le pattern 'id='.
    position = re.search(pattern=r'(?<=id=)\d+', string=line_1).group()
    
    # On utilise un lookbehind pour capturer le premier caractère qui suit le pattern 'body='.
    caractere = re.search(pattern=r'(?<=body=).', string=line_2).group()

    tuples.append((int(position), caractere))

tuples.sort(key=lambda tpl: tpl[0])

msg = [car[1] for car in tuples]
print(''.join(msg))

""" 
Salut Marco, la livraison du mardi est confirmée pour le 23 novembre au hangar des Forges, entrée par la rue Kellermann côté nord.
Prévoir trois véhicules, pas plus, et surtout aucun portable allumé pendant le transfert.
Le contact sur place répond au surnom de Mains-Froides, il portera une veste rouge et attendra à partir de 2h du matin.
La marchandise est répartie en quatorze colis identiques, ne pas les ouvrir avant d'avoir rejoint la planque d'Edimbourg.
En cas de problème, contacter uniquement la ligne chiffrée et détruire ce message après lecture.
La part de chacun sera versée en liquide dans les 48h suivant la livraison.
Ne fais confiance à personne d'autre qu'à ceux dont tu connais le visage.
"""
