
class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

class Init_Problem:
    def __init__(self):
        self.root = None

    def tree_node(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
            while 1:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

    def print_path(self, visited, goal):
        print('Path: ', end='')
        for i in range(len(visited)):
            if not (i == len(visited) - 1):
                print(visited[i], end='')
                print(' => ', end='')
            else:
                print(visited[i], end='')

    def create_tree(self):
        tree = [50, 25, 75, 18, 12, 14, 70, 92, 89,
               84, 28, 29, 33, 74, 61, 20, 22, 71,
               99, 96, 19, 26, 11, 27, 64, 91, 55]
        return tree