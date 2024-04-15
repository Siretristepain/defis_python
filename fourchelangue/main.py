
dic = {
 "HFH":"A",
 "FFH":"B",
 "SHS":"C",
 "SHH":"D",
 "SSH":"E",
 "FHF":"F",
 "FSS":"G",
 "HFF":"H",
 "HHH":"I",#J
 "SFS":"K",
 "FFS":"L",
 "FHS":"M",
 "SSF":"N",
 "FHH":"O",
 "HHF":"P",
 "SFF":"Q",
 "FSF":"R",
 "FSH":"S",
 "HHS":"T",
 "FFF":"U",#V
 "SSS":"W",
 "HFS":"X",
 "SHF":"Y",
 "SFH":"Z",
}

# Liste des clés du dictionnaire
keys = [key for key in dic.keys()]

# Ouverture du fichier
with open('input.txt', 'r') as f:
    msg = f.read()

# Traduction
traduction = []

# Résolution
for i in range(len(msg)-4):
    if i == 0:
        first = msg[i]
        second = msg[i+1]
        third = msg[i+2]
        syllabe = first + second + third

        if syllabe in keys:
            traduction.append(dic[syllabe])
        
        valide = True

    else:
        if valide == True:
            first = msg[i+2]
            second = msg[i+3]
            thid = msg[i+4]
            syllabe = first + second + third

            if syllabe in keys:
                traduction.append(dic[syllabe])
                valide  = True
            else:
                traduction.append(' ')
                valide = False

        elif valide == False:
            first = msg[i+1]
            second = msg[i+2]
            third = msg[i+3]
            syllabe = first + second + third

            if syllabe in keys:
                traduction.append(dic[syllabe])
                valide = True
            else:
                traduction.append(' ')
                valide = False

msg_traduit = ''.join(traduction)
print(f"Le message de Harry dit :\n{msg_traduit}")
        
