from math import inf
from queue import heappop, heappush
from collections import deque
from Initialization_Graph import Init_Problem


class Uniform_Cost(Init_Problem):
    def __init__(self):
        Init_Problem.__init__(self, directed=True)
        Init_Problem.__str__(self)

    def uniform_cost(self, start, goal, count):
        found, fringe, visited, came_from, cost_so_far\
            = False, [(0, start)], set([start]), {start: None}, {start: 0}

        while not found and len(fringe):
            _, current = heappop(fringe)
            count = count + 1

            if current == goal:
                found = True
                break
            for node in self.neighbors(current):
                new_cost = cost_so_far[current] + self.cost(current, node)
                if node not in visited or cost_so_far[node] > new_cost:
                    visited.add(node)
                    came_from[node] = current
                    cost_so_far[node] = new_cost
                    heappush(fringe, (new_cost, node))
                    count = count + 1

        if found:
            return came_from, cost_so_far[goal], count
        else:
            print('No path from {} to {}'.format(start, goal))
            return None, inf, count


graph = Uniform_Cost()
graph.create_graph2()
start, goal, count = 'A', 'Z', 0
trace, cost, count = graph.uniform_cost(start, goal, count)

if (trace):
    print('Path:', end=' ')
    graph.print_path(trace, goal)
    print('\nCost:', cost)
    print('Count:', count)