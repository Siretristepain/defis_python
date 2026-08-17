# ====================
# Ouverture du fichier
# ====================

with open("difficile_de_comprendre_un_lapin_cretin/src/input.txt", "r") as f:
    content = ''.join([line.split('\n')[0] for line in f.readlines()])


"""
Je pars du principe que chaque syllabe comporte 5 lettres et commence toujours par un B.
Il faut donc regarder les 5 premières lettres (=1ère syllabe), puis si la lettre suivante est différente de B, c'est qu'elle
fait partie du message. Et ainsi de suite.
La seule difficulé c'est que l'on ne peut pas faire une boucle for avec un pas de 5 en 5 car lorsqu'une lettre du message
est ajoutée, cela décale les syllabes.
"""
result = []

while content:
    syl = content[:6]
    if syl[-1] == 'B':
        content = content[5:]
    else:
        result.append(syl[-1])
        content = content[6:]

print(''.join(result))
# >>> ILFAUTTIRERLELEVIERETAPPUYERSURLEAOUTONJAUNEA