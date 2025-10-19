compteur=0

for i in range(1,51):
    nb_pomme=i**2
    if nb_pomme%3==0:
        compteur=compteur+nb_pomme

print(compteur)