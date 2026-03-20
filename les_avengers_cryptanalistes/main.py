from utile.cryptographie import vigenere_find_key, vigenere_decrypt_text

TEXT = "CJKDPQZZZLSULOEXFPNMXOSVLJSVRHRMFFOABIKBZFJM".lower()

for i in range(len(TEXT) - 6):
    crypt_text = TEXT[i:i+7]
    
    potential_key = vigenere_find_key(text_crypt=crypt_text, text_wish="proxima")
    print(potential_key)
    
    # for j in range(7):
    #     print(vigenere_decrypt_text(text=TEXT[j:], key=potential_key))
    # print(vigenere_decrypt_text(text=TEXT[i:], key=potential_key))


print(f"Le message déchiffré avec la clé 'loki' est : {vigenere_decrypt_text(text=TEXT, key="loki")}")

#--> Le message déchiffré avec la clé 'loki' est : rvavecproximaaupubdemainavingtheuresquatorze
