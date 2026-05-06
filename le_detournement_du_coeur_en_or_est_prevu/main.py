import utile.cryptographie as crypto

TEXT = "OIJXO GYXEJ WTDTD EJAOI CKHWT DKNED BTEBO WEOIP ZJLMJ SPEPC WWMVE HQFTI LVYOU XLCVX EIWFA VQRIS HNFYF HRCZI REMYO IWFZY FLRVM"
TEXT = "XXXXX XXXXX XXXXX XXXXX XXXXX XXXXX XXXXX XXXXX XXXXX XXXXA ISSEA UCOXX XXXXX XXXXX XXXXX XXXXX XXXXX XXXXX XXXXX XXXXX XXXXX"
TEXT = "XXXXX XXXXX XXXXX XXXXX XXXXX XXXXX XXXXX XXXXX XXXXX XXXXA ISSEA UCOEU RENOR POURL ADXXX XXXXX XXXXX XXXXX XXXXX XXXXX XXXXX"


# print(crypto.vigenere_crypt_letter("e", "t"))

print(crypto.vigenere_all_potential_keys(text_crypt=TEXT.lower(), existing_word="coeurenor", indexed_keys=True))

print(crypto.vigenere_decrypt_text(text="CWWMVEHQFTILVYOU".lower(), key="aisseaucoeurenor"))
print(crypto.vigenere_decrypt_text(text="PCWWMVEHQFTILVYOUXLCVXEI".lower(), key="vaisseaucoeurenorpourlad"))