from itertools import combinations_with_replacement

def only_2_and_4(n):
    return all(c in '24' for c in str(n))

best = None
best_count = -1

for a, b, c in combinations_with_replacement(range(1, 1000), 3):
    s = a + b + c
    p = a * b * c
    if only_2_and_4(s) and only_2_and_4(p):
        count_4 = str(a).count('4') + str(b).count('4') + str(c).count('4')
        if count_4 > best_count:
            best_count = count_4
            best = (a, b, c)
            print(f"Nouveau meilleur : {a}, {b}, {c} | somme={s} | produit={p} | nb de 4 = {count_4}")

print(f"\nRéponse finale : {best[0]}, {best[1]}, {best[2]}")