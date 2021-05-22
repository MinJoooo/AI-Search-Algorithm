from Initialization_Tree import Node, Init_Problem


class Tree(Node, Init_Problem):
    def __init__(self):
        Init_Problem.__init__(self)
        Init_Problem.__str__(self)

    def tree_algorithm(self, node, visited):
        if node is not None:
            visited.append(node.info)
            self.tree_algorithm(node.left, visited)
            self.tree_algorithm(node.right, visited)

        return visited


tree = Tree()
tree_model = tree.create_tree()
for i in tree_model:
    tree.tree_node(i)

goal, visited = 96, []
visited = tree.tree_algorithm(tree.root, visited)
tree.print_path(visited, goal)
print('\nCount:', len(visited))