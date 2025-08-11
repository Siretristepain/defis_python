from alphabet import alphabet

text = "REJOIGNEZNOUSETPARTAGEZVOTREPASSIONPOURLAPROGRAMMATIONAJOUTEZVOTRENOMAUHALLOFFAMEDESPLUSFINSPROGRAMMEURS"

result = 0

for i in text:
    result += alphabet[i.lower()]

print(result)