# ==================================
# Implémentation d'une liste chaînée
# ==================================

class Maillon():
    def __init__(self):
        self.val = None
        self.suiv = None

class ListeChainee():
    def __init__(self):
        self.tete = None

    def is_empty(self):
        """
        Méthode permettant de savoir si la liste chaînée est vide.

        Returns:
            - (bool) : True si liste vide, False sinon.
        """
        return self.tete == None
    
    def get_size(self):
        """
        Méthode permettant de retourner la taille de la liste chaînée.

        Returns:
            - size (int) : la taille de la liste chaînée.

        Complexité : O(n) -> c'est à dire que pour une liste de taille n, on parcours les n maillons pour en déduire la taille.
        """

        size = 0

        # On check si la liste chaînée est vide, auquel cas on retourne directement 0.
        if self.is_empty():
            return size
        
        # Si la liste chaînée n'est pas vide, on prends le noeud de tête comme premier maillon et on les parcours 1 à 1 en incrémentant un compteur.
        size += 1
        maillon = self.tete

        while maillon.suiv:
            size += 1
            maillon = maillon.suiv
        
        return size
    
    def get_last_maillon(self):
        """
        Méthode permettant de retourner le dernier maillon de la liste chaînée (le dernier noeud).
        Attention, la méthode ne retourne pas la valeur du dernier maillon mais bel et bien l'objet "maillon".

        Returns:
            - maillon (class Maillon()) : le dernier maillon de la liste chainée (=None si liste chaînée vide).

        Complexité : O(n) -> Pour une liste de taille n, on parcours les n maillons pour retourner le dernier.
        """

        # On fait appel à notre méthode get_size() pour obtenir la taille de la liste chaînée et on instaure la tête de la chaîne comme premier maillon.
        size = self.get_size()
        maillon = self.tete

        if size == 0:
            return maillon
        
        # On créer un compteur dont on va se servir en le comparant à la valeur retournée par get_size() durant le parcours de tous les maillons de la chaîne.
        i = 1

        # Temps que notre compteur n'est pas égal à la taille de la chaîne, on passe au maillon suivant en incrémentant de 1 notre compteur.
        while i != size:
            maillon = maillon.suiv
            i += 1

        return maillon
    
    def get_maillon_index(self, i):
        """
        Méthode qui permet de retourner le maillon d'indice i de la liste chaînée.
        Attention, le premier élément de la liste chaîne est considéré d'indice 0. Le second d'indice 1 etc... Comme avec les List Python classiques.

        Args:
            - i (int) : l'index du maillon de la chaîne que l'on souhaite récupérer.

        Returns:
            - maillon (class Maillon()) : le maillon d'index i de la liste chaînée.

        Complexité : O(n) -> Pour une liste chaînée de n maillons, si on veut le maillon d'indice n on doit parcourir les n maillons de la liste.
        """

        # On commence par récupérer la taille de la liste chaînée.
        size = self.get_size()

        # On s'assure que la valeur de i passée en argument de la méthode ne soit pas hors de la taille de la liste chaînée.
        if i < 0 or i >= size:
            return ValueError(f"La valeur d'index {i} passée en argument de la méthode get_maillon_index() n'est pas correcte pour la chaîne {self}.")
        
        # On initialise un compteur 'index' à 0 et le maillon de tête comme premier maillon
        index = 0
        maillon = self.tete

        # Temps que l'index (=notre compteur) n'est pas égal à l'index passé en argument (=index souhaité), on boucle sur chaque maillon de la liste en incrémentant de 1 notre compteur d'index.
        while index != i:
            maillon = maillon.suiv
            index += 1

        return maillon

    def add_at_begin(self, maillon):
        """
        Méthode pour ajouter un nouveau maillon au début de la liste chaînée (le noeud ajouté devient le nouveau noeud de tête de la chaîne).

        Args:
            - maillon (class Maillon()) : l'objet Maillon à ajouter au début de la liste.

        Returns:
            - (bool) : True.

        Complexité : O(1) -> Pour ajouter un maillon au début d'une liste de n élément, on a juste a ajouter un élément au début et le faire pointer
        sur l'ancien premier. Donc pas la peine d'itérer sur les n éléments.
        """

        # Si la liste est initialement vide, on se contente d'ajouter le nouveau maillon comme noeud de tête
        if self.is_empty():
            self.tete = maillon
            return True

        # Si la liste n'est pas initialement vide, il faut en plus faire pointer le pointeur du nouveau noeud de tête vers l'ancien noeud de tête (qui est décalé à l'index 1).
        first_maillon = self.get_maillon_index(0)
        self.tete = maillon
        maillon.suiv = first_maillon

        return True

    def add_at_end(self, maillon):
        """
        Méthode pour ajouter un nouveau maillon à la fin de la liste chaînée.

        Args:
            - maillon (class Maillon()) : l'objet Maillon à ajouter à la fin de la liste.

        Returns:
            - (bool) : True.

        Complexité : O(n) -> Pour ajouter un maillon à la fin d'une liste de n éléments, on doit récupérer le dernier élément et de le faire
        pointer sur le nouveau maillon. Du coup, on parcours implicitement les n éléments via la méthode get_last_maillon().
        """

        # Si la liste est initialement vide, on se contente d'ajouter le nouveau maillon comme noeud de tête
        if self.is_empty():
            self.tete = maillon
            return True

        # Si la liste n'est initialement pas vide, on récupère le dernier noeud de la liste et on le fait pointer vers le nouveau maillon ajouté.
        last_maillon = self.get_last_maillon()
        last_maillon.suiv = maillon

        return True

    def add_after_index(self, index, maillon):
        """
        Méthode qui permet d'insérer un nouveau maillon 'maillon' après le maillon d'indice 'index' dans la liste chaînée.

        Args:
            - index (int) : index du maillon après lequel on souhaite ajouter le nouveau maillon.
            - maillon (class Maillon) : le maillon à ajouter.

        Returns:
            - (bool) : True.

        Compléxité : O(n) -> Implicitement par l'appel à get_maillon_index().
                     Il serait possible d'implémenter une nouvelle méthode comme add_after_maillon(self, M1, M2) pour insérer
                     un maillon M2 après le maillon M1 et on pourrait faire ça en compléxité O(1) mais ça implique d'avoir
                     déjà les objets M1 ET M2. Donc la compléxité O(n) a de forte chance de se retrouver dans le code avant l'appel
                     de la méthode pour retrouver M1 et M2.
        """

        # On récupère le maillon d'indice 'index' (M(i)) et on récupère le maillon vers lequel il pointe (M(i+1)).
        maillon_before = self.get_maillon_index(index)
        next_maillon = maillon_before.suiv

        # Ajout du nouveau maillon (Mnew) : On fait pointer M(i) vers Mnew et Mnew vers M(i+1)
        maillon_before.suiv = maillon
        maillon.suiv = next_maillon

        return True

L = ListeChainee()
M1, M2 = Maillon(), Maillon()
M1.val = 1
M2.val = 2
M1.suiv = M2
L.tete = M1


M3 = Maillon()
M3.val = 3

L.add_after_index(0, M3)
print(L.get_size())
print(L.get_last_maillon().val)
print(L.get_maillon_index(1).val)
