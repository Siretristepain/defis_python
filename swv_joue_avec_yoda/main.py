# Ouvrir le fichier et récupérer la liste de tous les mots
with open("swv_joue_avec_yoda/src/input.txt", "r") as f:
    words = f.read().split(' ')

# print(words)
LENGTH = len(words)

# On créer la fonction
def find_next_word(word: str, words: list[str]):
    next_word = ''
    for w in words:
        if w.startswith(word[-3:]):
            next_word = w
            break

    if next_word == '':
        print('Erreur. Mot non trouvé dans la liste.')

    return next_word

# Test pour voir si la fonction a bien le comportement attendu
# print(find_next_word(word="bonjour", words=["happy", "test", "bonbon", "bouteille", "ours"]))
# --> 'ours'

def solve_for_one_word(word: str, words: list[str], show_output: bool = False):
    words_copy = words.copy()
    result = [word]
    words_copy.remove(word)
    running = True

    while running:
        next_word = find_next_word(word=word, words=words_copy)

        if next_word == '' or words == []:
            running = False
        
        else:
            result.append(next_word)
            word = next_word
            words_copy.remove(word)

    if show_output:
        print(result)
        print(len(result))

    return len(result) == LENGTH

print(solve_for_one_word(word=words[3], words=words, show_output=True))

# i = 0
# for word in words:
#     if solve_for_one_word(word=word, words=words) == True:
#         solve_for_one_word(word=word, words=words, show_output=True)
#         break
        
#     else:
#         print(f"Not {word}")

#     i += 1

# print(i)
# print(LENGTH)