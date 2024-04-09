


for i in range(1,1000000):
#for i in range(1):
    nb_gallion = i
    nb_mornille = 17*i
    nb_noise = nb_mornille*29
    
    gallion_set = set([*str(nb_gallion)])
    mornille_set = set([*str(nb_mornille)])
    noise_set = set([*str(nb_noise)])

    if gallion_set == mornille_set == noise_set :
        print('*'*20)
        print(f"La somme laissée par Sirius pour Harry est de {i} gallions.")
        print('*'*20)
        break

