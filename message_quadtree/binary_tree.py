# ===========================================
# Implémentation d'un arbre binaire en Python
# ===========================================

class Node():
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"Node value : {self.val}, left : {self.left.val}, right : {self.right.val}"
    
    def is_null(self):
        return self.val == None
    
    def is_leaf(self):
        return self.left == None and self.right == None

class BinaryTree():
    def __init__(self, head=None):
        self.head = head

    def is_empty(self):
        """
        Une arbre est vide s'il n'a pas de noeud racine (head).

        Returns:
            - (bool) : True si arbre vide, False sinon.
        """
        return self.head == None
    
    def height(self):
        """
        Méthode récursive qui retourne la hauteur de l'arbre.
        La hauteur d'un arbre corresponds à son nombre de "strates".

        Pour un arbre vide, la hauteur vaut 0.
        Pour un arbre non vide, la hauteur vaut 1 + la hauteur la plus élévée entre son sous-arbre gauche et son sous-arbre droit.

        Returns:
            - (int) : la hauteur de l'arbre.
        """

        # Si l'arbre est vide, on retourne 0.
        if self.is_empty():
            return 0
        
        # Si l'arbre n'est pas vide, on sait qu'il a alors une hauteur d'au moins 1.
        # Ensuite, on créer le sous arbre gauche et le sous arbre droit.
        # Sur chacun de ces sous-arbres, on rappelle la méthode height (qui vas donc récursivement parcourir tous les sous-arbres de l'arbre original jusqu'à arriver aux arbres vide).
        # On récupère le sous-arbre le plus long.
        return 1 + max(BinaryTree(head=self.head.left).height(), BinaryTree(head=self.head.right).height())

        


"""
            1
           / \
          /   \
         /     \
        2       3
       / \       \
      /   \       \
     4     5       6
            \
             \
              7
"""
N1, N2, N3, N4, N5, N6, N7 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7)
N1.left = N2
N1.right = N3
N2.left = N4
N2.right = N5
N5.left = N7
N3.left = N6

AB = BinaryTree()
AB.head = N1

print(AB.height())
