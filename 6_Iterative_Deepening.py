from math import inf
from queue import heappop, heappush
from collections import deque
from Initialization_Graph import Init_Problem


class Iterative_Deepening(Init_Problem):
    def __init__(self):
        Init_Problem.__init__(self, directed=True)
        Init_Problem.__str__(self)

    def iterative_deepening(self, start, goal, count):
        prev_iter_visited, depth = [], 0
        while True:
            traced_path, visited, count = self.depth_limited_search(start, goal, depth, count)
            if traced_path or len(visited) == len(prev_iter_visited):
                return traced_path, count
            else:
                prev_iter_visited = visited
                depth = depth + 1

    def depth_limited_search(self, start, goal, limit=-1, count=0):
        found, fringe, visited, came_from =\
            False, deque([(0, start)]), set([start]), {start: None}

        while not found and len(fringe):
            depth, current = fringe.pop()

            if current == goal:
                found = True
                break
            if limit == -1 or depth < limit:
                for node in self.neighbors(current):
                    if node not in visited:
                        visited.add(node)
                        fringe.append((depth + 1, node))
                        came_from[node] = current
                        count = count + 1

        if found:
            print('\nLimit {}'.format(limit))
            return came_from, visited, count
        else:
            print('Limit {}: No path from {} to {}'.format(limit, start, goal))
            return None, visited, count


graph = Iterative_Deepening()
graph.create_graph()
start, goal, count = 'A', 'Z', 0
trace, count = graph.iterative_deepening(start, goal, count)

if trace:
    print('Path:', end=' ')
    graph.print_path(trace, goal)
    print('\nCount:', count)