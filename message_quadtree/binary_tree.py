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
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def height(self):

        node = self.head
        count = 0
        
        if self.is_empty():
            return count
        
        # Pour l'instant je choisis arbitrairement de prendre le noeud enfant gauche comme noeud suivant mais ce n'est pas rigoureux.
        # Je ne vois pas comment faire pour à la fois partir sur le sous arbre gauche et le sous arbre droit.
        # Il faudrait faire l'opération sur 2 objets en même temps, puis sur 4 au suivant, puis sur 8 etc...
        while not node.is_leaf():
            count += 1
            node = node.left
        
        return count


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
