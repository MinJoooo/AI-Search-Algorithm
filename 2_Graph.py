from Initialization_Tree import Node, Init_Problem


class Graph(Node, Init_Problem):
    def __init__(self):
        Init_Problem.__init__(self)
        Init_Problem.__str__(self)

    def graph_algorithm(self, visited):
        self.root.level = 0
        queue = [self.root]
        current_level = self.root.level

        while len(queue) > 0:
            current_node = queue.pop(0)
            visited.append(current_node)

            if current_node.level > current_level:
                current_level += 1

            if current_node.left:
                current_node.left.level = current_level + 1
                queue.append(current_node.left)

            if current_node.right:
                current_node.right.level = current_level + 1
                queue.append(current_node.right)

        return visited


tree = Graph()
tree_model = tree.create_tree()
for i in tree_model:
    tree.tree_node(i)

goal, visited = 96, []
visited = tree.graph_algorithm(visited)
tree.print_path(visited, goal)
print('\nCount:', len(visited))