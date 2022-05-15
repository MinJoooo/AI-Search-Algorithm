from math import inf
from queue import heappop, heappush
from collections import deque
from Initialization_Graph import Init_Problem

class RBFS(Init_Problem):
    def __init__(self):
        Init_Problem.__init__(self, directed=True)
        Init_Problem.__str__(self)
        self.heuristics = {}

    def iterative_deepening(self, start, goal, count):
        prev_visited, depth = 0, 0
        while True:
            trace, cost, visited, count = self.depth_limited_search(start, goal, depth, count)
            if trace or visited == prev_visited:
                return trace, cost, count
            prev_visited = visited
            depth = depth + 1

    def depth_limited_search(self, start, goal, limit=-1, count=0):
        found, fringe, visited =\
            False, [(self.heuristics[start], start, 0)], set([start])
        came_from, cost_so_far = {start: None}, {start: 0}

        while not found and len(fringe):
            _, current, depth = heappop(fringe)

            if current == goal:
                found = True
                break
            if limit == -1 or depth < limit:
                for node in self.neighbors(current):
                    new_cost = cost_so_far[current] + self.cost(current, node)
                    if node not in visited or cost_so_far[node] > new_cost:
                        visited.add(node)
                        came_from[node] = current
                        cost_so_far[node] = new_cost
                        heappush(fringe, (new_cost + self.heuristics[node], node, depth + 1))
                        count = count + 1

        if found:
            print('\nLimit {}'.format(limit))
            return came_from, cost_so_far[goal], len(visited), count
        else:
            print('Limit {}: No path from {} to {}'.format(limit, start, goal))
            return None, inf, len(visited), count


graph = RBFS()
graph.create_graph2()
graph.create_heuristics()
start, goal, count = 'A', 'Z', 0
trace, cost, count = graph.iterative_deepening(start, goal, count)

if trace:
    print('Path:', end=' ')
    graph.print_path(trace, goal)
    print('\nCost:', cost)
    print('Count:', count)