class Boite:
    def __init__(self, name: str, state: int, **kwargs):
        self.name = name
        self.state = state
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return "{}: {}".format(self.name, self.state)

    def compute_output(self):
        output = self.outputs[self.state - 1]
        self.state = (self.state + 1) % len(self.outputs)
        return output


# ================================
# Création des 6 intances de Boite
# ================================

b1 = Boite(name="B1", state=1, outputs=["B2", "B3", "B4"])
b2 = Boite(name="B1", state=1, outputs=["B5", "B6"])
b3 = Boite(name="B1", state=1, outputs=["B2", "B5", "B6"])
b4 = Boite(name="B1", state=1, outputs=["B3", "B6"])
b5 = Boite(name="B1", state=1, outputs=["ROCHE", "EAU"])
b6 = Boite(name="B1", state=1, outputs=["B5", "GLACE", "B4"])

# =========================================================
# Dictionnaire de correspondance "nom" -> instance de Boite
# =========================================================

boites = {
    "B1": b1,
    "B2": b2,
    "B3": b3,
    "B4": b4,
    "B5": b5,
    "B6": b6,
}

# ==========
# Itérations
# ==========

TARGET = ["ROCHE","EAU","GLACE"]
result = []

for i in range(100):

    # Conditions initiales
    boite = b1
    output = None

    while output not in TARGET:
        # On regarde la sortie de la boite courante en fonction de son 'state'.
        # Si c'est un des TARGET, on stop l'itération en cours, sinon, on prépare l'itération suivante avec la prochaine boite.
        boite_output_name = boite.compute_output()
        if boite_output_name in TARGET:
            break
        boite = boites.get(boite_output_name)

    result.append(boite_output_name[0])

print("".join(result))
# REREGRERGERGERGERERGEREGRERGERGEREGRERGEREGREGRERGEREGRERGEREGRERGERGEREGRERGEREGREREGRERGERGERGERER
