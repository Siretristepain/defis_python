import re

with open("cuisine_dentrassis/src/input.txt", "r") as f:
    content = [line.split('\n')[0] for line in f.readlines()]

# =========
# Fonctions
# =========

def ordered_each_recip(all_recip: list[str]) -> list[dict]:
    ordered_recip = []

    for recip in all_recip:
        ref = re.search(r'^.', recip).group()
        name = re.search(r'(?<=:\s).*?(?=\s:)', recip).group()
        prep = re.search(r'\d+', recip).group()
        cuis = re.search(r'\d{1,2}(?=\D*$)', recip).group()

        ordered_recip.append({
            'ref': ref,
            'name': name,
            'prep': int(prep),
            'cuis': int(cuis),
            'ratio': int(prep) / int(cuis),
            'effective_prep': 0,
            'effective_cuis': 0
        })

    ordered_recip.sort(key=lambda recip: recip['ratio'])

    return ordered_recip

# for recip in ordered_each_recip(content):
#     print(recip)

# ====
# Loop
# ====

incrementation = 0
finish_recip = 0
prep_index = 0

prep_done = []
result_prep = []
result_cuis = []

all_recip = ordered_each_recip(content)


while (finish_recip < 30 or prep_done != []):
# for i in range(2):

    # =======
    # Cuisson
    # =======

    # On choisi la recette a mettre au four en prenant la recette en file d'attente depuis le plus longtemps.
    if prep_done:
        # ==========================================================================================================================================================
        # /!\ Initialement, pour choisir le plat à mettre au four, je pensais qu'il fallait prendre celui dans la file d'attente avec le plus long temps de cuisson.
        # Finallement, il suffit de prendre celui en file d'attente depuis le plus longtemps ...
        # ==========================================================================================================================================================
        # prep_done.sort(key=lambda recip: recip['cuis'], reverse=True)
        current_cuis = prep_done[0]
        result_cuis.append(current_cuis['ref'])

        # On rajoute 5 min a son temps de cuisson.
        current_cuis['effective_cuis'] += 5

        # On check si la cuisson est terminée
        if current_cuis['effective_cuis'] == current_cuis['cuis']:

            # On incrémente de 1 le nombre de plat terminés
            finish_recip += 1

            # On retire le plat de la file d'attente de cuisson
            prep_done.remove(current_cuis)
    
    # Cas particulier du début où il n'y que des préparations mais pas encore de cuissons.
    else:
        result_cuis.append('.')

    # ===========
    # Préparation
    # ===========

    # On récupère la recette qu'on est actuellement en train de préparer.
    if prep_index <= len(all_recip) - 1:
        current_prep = all_recip[prep_index]
        result_prep.append(current_prep['ref'])

        # On ajoute 5 min à son temps de préparation
        current_prep['effective_prep'] += 5

        # On check si la recette est fini de préparer.
        if current_prep['effective_prep'] == current_prep['prep']:

            # On place la recette préparée dans la liste d'attente pour la cuisson.
            prep_done.append(current_prep)

            # On passe à la recette a préparer suivante.
            prep_index += 1
    
    # Cas particulier à la fin, où tous les plats auront été préparés mais où il restera uniquement des cuissons.
    else:
        result_prep.append('.')

    incrementation +=1



# print(''.join(result))

result = []

for i in range(len(result_prep)):
    result.append(result_prep[i])
    result.append(result_cuis[i])
    # print(result_prep[i])
    # print(result_cuis[i])
    # print('-'*5)

print(f"Temps total : {incrementation*5} min.")
print(''.join(result))
# Résultat faux en prenant pour la cuisson le plat en file d'attente avec le plus long temps de cuisson:
# --> L.aLELELkLkLGLGLHLHLmLmEeEeEeEeEeEMEMEMEMEgegegegegegegegeJeJgJgJgJgJgJgJgAgAgAJAJAJAJAJoJoJBJBJBkBkBkBkBkBkBkiBiBiBiBiBiBiBiBiAOiOiOiOiOiOiOiOiOAhOhOhOhOhOhOhOCOCACACACACACGCGlGlGlGlGlHlHlHlHnHnHnMnMbMbMbMbMbhbhbhdhdhdhdCdCcCcCcCcCclclclclclclfafafafafaIbIbIbIbIbImImImImIcNcNcNcNININININnNnNnDNDNDNDNDdDdDdDoDoFDFDFDFfFfF.F.F.F.F.jFjFjFj.j.KjK.K.K.K.K.K.K.K..K

# Résultat juste en prenant pour la cuisson le plat en file d'attente depuis le plus longtmps:
# --> L.aLELELkLkLGLGLHLHLmLmaeaeaeaeaeEMEMEMEMEgEgEgEgEgEgkgkgkJkJkJkJkJGJGJGJGAGAGAHAHAHAHAHoHomBmBmBmBeBeBeBeBeBeieieieiMiMiMiMiMiMOgOgOgOgOgOgOgOgOghJhJhJhJhJhJhJCJCJCACACACACACAlAlololBlBlBlBlBnBnBnBnibibibibibibibidOdOdOdOdOcOcOcOchchchchchchcCfCfCfCfCfCIlIlIlIlIlIlInInInIbNbNbNbNbNdNdNdNcNcNcDcDfDfDIDIDIDIDNDNFNFNFDFDFDF.F.F.F.F.jFjFjFj.j.KjK.K.K.K.K.K.K.K..K

# print(len(result)/2)

# /!\ Ce que je ne comprends pas vraiment, c'est que peut importe la stratégie de sélection du plat pour la cuisson, le temps total est le même : 181 itérations, soit 905 min.
# Donc les 2 solutions sont correctes et a priori équivalentes j'imagine.
