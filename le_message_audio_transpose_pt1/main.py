import wave

# ==========================================
# Table de transposition et fonction inverse
# ==========================================

transpo_table = [15, 103, 144, 224, 209, 205, 196, 130, 128, 191,  25,  90,  70,  48, 229, 161,
219,  92,   9, 134, 186, 121, 238,  12, 118, 139, 184, 231, 108, 160, 162,  42,
154, 233, 133, 204, 253, 129, 132,  93, 137, 251, 235, 167,  98,  52, 115, 201,
 61, 177, 126, 216,  27, 142, 234, 245, 168,   2,  60, 105, 147,  87, 155, 116,
172,  57, 206, 189, 176, 114,  21,  64, 101, 179, 212, 195, 249, 171,  78, 146,
192,  99, 199,   4, 241, 106,  14, 242,  94, 169, 131,  82,  86, 158, 136,  77,
 89,  72, 138, 210,  22,  62,  83, 181,  17,  80, 180, 113, 237,  58,  63,  53,
 40, 166, 243, 140,  10, 203, 239,  23,  32, 211, 175, 220,  33, 152,  31,   5,
110, 149, 254,   1, 185, 255,  59, 246, 107,  18,  50,  36, 240, 188, 244,  45,
150, 193,  51, 232, 174, 165,  35,  68,  47,  20, 247, 222, 123,  39,  43, 187,
 44,   7,  66, 157,  96, 112,   8, 164, 218, 111, 127,  38, 252, 102, 230,  91,
225, 182,  54,  16, 213,  24, 117, 170, 100, 141, 156,  81, 202,  19,  30, 250,
145, 173,  95, 208, 207, 223, 124,   3, 143,  49,   0,  11, 104, 125, 215,  88,
 28,  55,  85, 226, 120, 248,  76,  46, 135, 236, 200,   6, 178, 228,  34,  56,
 69, 190, 194, 122, 148,  67,  37, 153,  65,  97, 214,  75, 217,  29, 198,  74,
221,  79, 159, 197,  41, 151,  13, 109,  84,  26, 163, 227, 119,  73, 183,  71]

def transposition(octet) -> int:
    index = transpo_table.index(octet)
    return index

# ===========================================
# Lecture octet par octet du fichier d'entrée
# ===========================================

correct_octet = []

with wave.open("le_message_audio_transpose_pt1/src/chiffre_message_B.wav") as input_file:

    # Récupération des métadonnées du fichier d'entrée.
    metadata = input_file.getparams()

    nchannels = metadata.nchannels
    sampwidth = metadata.sampwidth
    framerate = metadata.framerate

    # Récupération des octets non signés du fichier d'entrée.
    frames = input_file.readframes(metadata.nframes)

    for oct in frames:
        transpo_value = transposition(oct)
        correct_octet.append(transpo_value)

# Sûr de fermer le fichier (même si pas nécessaire avec with())
input_file.close()

# =============================================
# Ecriture octet par octet du fichier de sortie
# =============================================

with wave.Wave_write("le_message_audio_transpose_pt1/src/output.wav") as output:

    # On écrit les mêmes métadatas dans le fichier de sortie que celles présentes dans le fichier d'entrée.
    output.setnchannels(nchannels)
    output.setsampwidth(sampwidth)
    output.setframerate(framerate)

    # On écrit la valeur de chaque bit dans le fichier de sortie.
    for oct in correct_octet:
        output.writeframes(oct.to_bytes(1, 'big'))

# Sûr de fermer le fichier (même si pas nécessaire avec with())
output.close()

# --> "Dans l'appartement vide du 42 Carnaby Street, c'est dans le clavecin qu'il faut regarder."
