class Quadtree():

    def __init__(self):
        self.root = Node(value="+", parent_node=False, children=[], root=True)

    def __repr__(self):
        return f"Quadtree avec noeud root --> {self.root}."

    def add_node(self, node_value):
        pass

class Node():
    def __init__(self, value, parent_node, children, root=False):
        self.check_validation(value, parent_node, children, root)
        self.value = value
        self.parent_node = parent_node
        self.children = children

    def __repr__(self):
        return f"Noeud : {self.value}, parent : {self.parent_node}, enfants : {self.children}."

    def check_validation(self, value, parent_node, children, root=False):
        if root:
            if not parent_node == False:
                raise ValueError("Le noeud root ne peut pas avoir de parent.")
        elif value in ['B', 'N']:
            if children:
                raise ValueError("Un noeud B/N ne peut pas avoir d'enfant.")
            if parent_node in ['B', 'N']:
                raise ValueError("Un noeud B/N ne peut pas être enfant d'un noeud B/N.")
        elif value == '+':
            if not len(children) == 4:
                raise ValueError("Un noeud + doit avoir 4 enfants.")
            if parent_node in ['B', 'N']:
                raise ValueError("Un noeud + ne peut pas avoir un noeud B/N comme parent.")

a = Node(value='+', parent_node='+', children=['B', 'B', 'B', 'B'])
b = Quadtree()
print(b)

