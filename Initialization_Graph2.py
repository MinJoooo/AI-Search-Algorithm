from math import inf
from queue import heappop, heappush
from collections import deque

class Init_Problem:
    def __init__(self, directed=True):
        self.edges = {}
        self.directed = directed

    def edge(self, node1, node2, __reversed=False):
        try: neighbors = self.edges[node1]
        except KeyError: neighbors = set()
        neighbors.add(node2)
        self.edges[node1] = neighbors
        if not self.directed and not __reversed:
            self.edge(node2, node1, True)

    def edge2(self, node1, node2, cost = 1, __reversed=False):
        try: neighbors = self.edges[node1]
        except KeyError: neighbors = {}
        neighbors[node2] = cost
        self.edges[node1] = neighbors
        if not self.directed and not __reversed:
            self.edge2(node2, node1, cost, True)

    def set_heuristics(self, heuristics={}):
        self.heuristics = heuristics

    def neighbors(self, node):
        try: return self.edges[node]
        except KeyError: return []

    def cost(self, node1, node2):
        try: return self.edges[node1][node2]
        except: return inf

    def print_path(self, came_from, goal):
        parent = came_from[goal]
        if parent:
            self.print_path(came_from, parent)
        else:
            print(goal, end='')
            return
        print(' =>', goal, end='')

    def __str__(self):
        return str(self.edges)

    def create_graph(self):
        self.edge('A', 'B')
        self.edge('A', 'C')
        self.edge('B', 'D')
        self.edge('C', 'L')
        self.edge('C', 'O')
        self.edge('D', 'E')
        self.edge('D', 'H')
        self.edge('D', 'L')
        self.edge('E', 'F')
        self.edge('F', 'G')
        self.edge('G', 'H')
        self.edge('G', 'I')
        self.edge('H', 'K')
        self.edge('I', 'J')
        self.edge('J', 'K')
        self.edge('K', 'M')
        self.edge('L', 'K')
        self.edge('M', 'N')
        self.edge('N', 'V')
        self.edge('O', 'P')
        self.edge('O', 'U')
        self.edge('P', 'Q')
        self.edge('P', 'R')
        self.edge('Q', 'S')
        self.edge('R', 'T')
        self.edge('S', 'T')
        self.edge('T', 'U')
        self.edge('U', 'V')
        self.edge('V', 'W')
        self.edge('V', 'Y')
        self.edge('W', 'X')
        self.edge('X', 'Z')
        self.edge('Y', 'Z')

    def create_graph_bidirectional(self):
        self.edge('A', 'B')
        self.edge('A', 'C')
        self.edge('B', 'D')
        self.edge('C', 'L')
        self.edge('C', 'O')
        self.edge('D', 'E')
        self.edge('D', 'H')
        self.edge('D', 'L')
        self.edge('E', 'F')
        self.edge('F', 'G')
        self.edge('G', 'H')
        self.edge('G', 'I')
        self.edge('H', 'K')
        self.edge('I', 'J')
        self.edge('J', 'K')
        self.edge('K', 'M')
        self.edge('L', 'K')
        self.edge('M', 'N')
        self.edge('N', 'V')
        self.edge('O', 'P')
        self.edge('O', 'U')
        self.edge('P', 'Q')
        self.edge('P', 'R')
        self.edge('Q', 'S')
        self.edge('R', 'T')
        self.edge('S', 'T')
        self.edge('T', 'U')
        self.edge('U', 'V')
        self.edge('V', 'W')
        self.edge('V', 'Y')
        self.edge('W', 'X')
        self.edge('X', 'Z')
        self.edge('Y', 'Z')

        self.edge('B', 'A')
        self.edge('C', 'A')
        self.edge('D', 'B')
        self.edge('L', 'C')
        self.edge('O', 'C')
        self.edge('E', 'D')
        self.edge('H', 'D')
        self.edge('L', 'D')
        self.edge('F', 'E')
        self.edge('G', 'F')
        self.edge('H', 'G')
        self.edge('I', 'G')
        self.edge('K', 'H')
        self.edge('J', 'I')
        self.edge('K', 'J')
        self.edge('M', 'K')
        self.edge('K', 'L')
        self.edge('N', 'M')
        self.edge('V', 'N')
        self.edge('P', 'O')
        self.edge('U', 'O')
        self.edge('Q', 'P')
        self.edge('R', 'P')
        self.edge('S', 'Q')
        self.edge('T', 'R')
        self.edge('T', 'S')
        self.edge('U', 'T')
        self.edge('V', 'U')
        self.edge('W', 'V')
        self.edge('Y', 'V')
        self.edge('X', 'W')
        self.edge('Z', 'X')
        self.edge('Z', 'Y')

    def create_graph2(self):
        self.__init__()
        self.edge2('A', 'B', 1)
        self.edge2('A', 'C', 1)
        self.edge2('B', 'D', 2)
        self.edge2('C', 'L', 3)
        self.edge2('C', 'O', 4)
        self.edge2('D', 'E', 4)
        self.edge2('D', 'H', 1)
        self.edge2('D', 'L', 1)
        self.edge2('E', 'F', 5)
        self.edge2('F', 'G', 3)
        self.edge2('G', 'H', 2)
        self.edge2('G', 'I', 3)
        self.edge2('H', 'K', 3)
        self.edge2('I', 'J', 1)
        self.edge2('J', 'K', 4)
        self.edge2('K', 'M', 2)
        self.edge2('L', 'K', 5)
        self.edge2('M', 'N', 1)
        self.edge2('N', 'V', 4)
        self.edge2('O', 'P', 2)
        self.edge2('O', 'U', 3)
        self.edge2('P', 'Q', 4)
        self.edge2('P', 'R', 1)
        self.edge2('Q', 'S', 5)
        self.edge2('R', 'T', 2)
        self.edge2('S', 'T', 1)
        self.edge2('T', 'U', 4)
        self.edge2('U', 'V', 5)
        self.edge2('V', 'W', 1)
        self.edge2('V', 'Y', 3)
        self.edge2('W', 'X', 1)
        self.edge2('X', 'Z', 3)
        self.edge2('Y', 'Z', 4)

    def create_heuristics(self):
        self.set_heuristics({
            'A': 2,
            'B': 1,
            'C': 3,
            'D': 1,
            'E': 4,
            'F': 2,
            'G': 4,
            'H': 2,
            'I': 1,
            'J': 5,
            'K': 3,
            'L': 5,
            'M': 3,
            'N': 1,
            'O': 4,
            'P': 1,
            'Q': 4,
            'R': 3,
            'S': 1,
            'T': 5,
            'U': 2,
            'V': 5,
            'W': 4,
            'X': 2,
            'Y': 2,
            'Z': 1
        })
