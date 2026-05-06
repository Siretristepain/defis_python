from __future__ import annotations

class Node:
    """
    Je viens de découvrir quelque chose d'important :

    Au début, j'avais fait def __init__(self, value: int, power: int = None, links: list = []):

    La différence c'est donc que j'avais une valeur par défaut pour links ---> [].
    Le problème, c'est que si on passe une valeur par défaut pour un objet MUTABLE, cette objet est commun pour toutes
    les instances de la classe.
    C'est à dire qu'en faisant ça, links était COMMUN à chaque instance.

    Ex :
    N000 = Node(0, 100)
    N001 = Node(1, 105)
    N002 = Node(2, 105)

    N000.links.append(N001)
    N001.links.append(N002)

    print(N000.links)
    ---> [Node 1, Node 2]
    Ce résultat est surprenant quand on voit que l'on a ajouté uniquement le Node 1 dans N000.links .

    Mais cela est du au fait que toutes les instances partage le même links.

    --> Ce comportement n'a lieu qu'avec les objets mutables python : list, set, dict.
    Les objets immutables n'ont pas ce comportement : int, str, tuple...

    Pour que chaque instance ait sa propre links, il faut faire comme suit :
    """

    # Variable de classe partagée par toutes les instances
    instances = []

    def __init__(self, value: int, power: int = None, links: list = None):
        self.value = value
        self.power = power
        self.links = [] if links is None else links
        Node.instances.append(self)

    def __repr__(self):
        return f"Node {self.value}"
    
    def is_linked(self, neighboor):
        if neighboor in self.links:
            return True
        return False
    
    def linked_to_power(self, power: int):
        neighboors = []
        for neigh in self.links:
            if neigh.power == power:
                neighboors.append(neigh)
        return neighboors
    
    @classmethod
    def get_all_instances(cls):
        return cls.instances
    
    @classmethod
    def search_node_with_corresponding_power(cls, power: int) -> list[Node]:
        result = []
        for node in cls.instances:
            if node.power == power:
                result.append(node)
        return result
    

if __name__ == '__main__':
    N000 = Node(0, 100)
    N001 = Node(1, 105)
    N002 = Node(2, 105)
    N003 = Node(3, 90)
    N004 = Node(4, 100)

    N000.links.append(N003)
    N000.links.append(N004)
    N001.links.append(N002)
    N002.links.append(N003)
    N003.links.append(N000)
    N004.links.append(N001)
    N004.links.append(N002)

    # print(N000.linked_to_power(100))
    powers = [100, 105, 90]

    # print(Node.get_all_instances())
    # print(Node.search_node_with_corresponding_power(90))

    head_nodes = Node.search_node_with_corresponding_power(power=powers[0])

    for head_node in head_nodes:
        second = head_node.linked_to_power(power=powers[1])
    print(second)
