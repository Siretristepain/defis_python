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

    def delete_start(self):
        """
        Méthode permettant de supprimer le permier maillon de la liste chaînée.

        Retuns:
            - deleted_tete (class Maillon) : le maillon supprimé (= le permier maillon de la liste avant suppression).
                                             Cas particulier où la méthode retourne True si la liste était vide au moment de l'appel à la méthode.

        Compléxité : O(1) -> On récupère juste le premier maillon de la liste et on supprime sa référence (suiv) et le self.tete de la liste.
                     Pas la peine de pacourir les n maillons de la liste.
        """

        # Si la liste est vide on ne fait rien.
        if self.is_empty():
            return True

        # Si la liste a au moins un maillon (donc au moins une tête), on la récupère pour pouvoir la retourner en sortie de la méthode et on change la valeur de la tête de la liste.
        deleted_tete = self.tete
        self.tete = self.tete.suiv

        return deleted_tete

    def delete_end(self):
        """
        Méthode pour supprimer le dernier maillon de la liste chaînée.

        Returns:
            - deleted_maillon (class Maillon) : le maillon supprimé. Cas particulier où la méthode retourne True si la liste était vide au moment de l'appel à la méthode.

        Compléxité : O(n) -> Car appel à la méthode get_last_maillon() qui parcours les n maillons de la liste chaînée.
        """

        # Si la liste est vide, on ne fait rien.
        if self.is_empty():
            return True

        size = self.get_size()

        # Si la liste n'a qu'un seul maillon (= la tête), on se contente de supprimer la référence self.tete
        if size == 1:
            deleted_maillon = self.tete
            self.tete = None
            return deleted_maillon

        # Si la liste à plus d'un maillon, on récupère le dernier (pour pouvoir le retourner), et on récupère l'avant dernier pour suppimer sa référence (suiv) vers le dernier.
        deleted_maillon = self.get_last_maillon()
        previous_last_maillon = self.get_maillon_index(size-2)
        previous_last_maillon.suiv = None

        return deleted_maillon

    def delete_after_index(self, index):
        """
        Méthode qui permet de supprimer le maillon d'indice index+1 dans la liste chaînée.

        Args:
            - index (int) : l'index du maillon qui précède celui que l'on veut supprimer.

        Returns:
            - deleted_maillon (class Maillon) : le maillon supprimé.

        Compléxité : O(n) -> Car appel à la méthode get_maillon_index() qui doit potentiellement parcourir les n maillons de la liste chaînée.
        """

        # On récupère le maillon qui précède celui a supprimer, on en déduit le maillon à supprimer et le maillon suivant.
        previous_maillon = self.get_maillon_index(index)
        deleted_maillon = previous_maillon.suiv
        next_maillon = deleted_maillon.suiv

        # Le maillon qui précède celui a supprimer pointe maintenant vers le maillon qui suivait celui qu'on a supprimé.
        previous_maillon.suiv = next_maillon

        return deleted_maillon

    def show(self):
        """
        Méthode qui permet d'avoir un petit rendu visuel des valeurs des maillons de la liste chaînée.

        Returns:
            - (str) : la représentation de la liste chaînée sous forme str.

        Compléxité : O(n**2) -> Car on boucle n fois sur les n maillons.

        Example:
            L = ListeChainee()
            M1, M2, M3 = Maillon(), Maillon(), Maillon()
            M1.val = 1
            M2.val = 2
            M3.val = 3
            M1.suiv = M2
            M2.suiv = M3
            L.tete = M1
            print(L.show())

            >>> 1 -> 2 -> 3
        """

        size = self.get_size()
        all_values = []

        for i in range(size):
            maillon = self.get_maillon_index(i)
            all_values.append(str(maillon.val))

        return ' -> '.join(all_values)
    
    def get_index(self, M):
        """
        Méthode qui permet de retourner l'index sur maillon passé en argument dans la ListeChainee.

        Args:
            - M (class Maillon) : le maillon dont on souhaite connaitre l'index dans la liste.

        Returns:
            - index (int) : l'index du maillon.
        """

        maillon = self.tete
        index = 0

        while maillon != M:
            maillon = maillon.suiv
            index += 1

        return index
    
    def add_after(self, M1, M2):
        next_maillon = M1.suiv
        M1.suiv = M2
        M2.suiv = next_maillon

    def add_before(self, M1, M2):
        M1_index = self.get_index(M1)
        # ??? Même avec un M1_index = 0, on a pas d'erreur en appelant get_maillon_index alors que l'argument sera -1 ???
        previous_M1 = self.get_maillon_index(M1_index-1)
        previous_M1.suiv = M2
        M2.suiv = M1

L = ListeChainee()
M1, M2, M3 = Maillon(), Maillon(), Maillon()
M1.val = 1
M2.val = 2
M3.val = 3
M1.suiv = M2
M2.suiv = M3
L.tete = M1

print(L.show())
M4 = Maillon()
M4.val = 4
L.add_before(M1, M4)
print(L.show())
# print(L.get_size())
# print(L.delete_after_index(1))
# print(L.get_size()) # --> 2
# print(L.get_last_maillon().val) # --> 2
