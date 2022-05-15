from math import inf
from queue import heappop, heappush
from collections import deque
from Initialization_Graph import Init_Problem


class Bidirectional(Init_Problem):
    def __init__(self):
        Init_Problem.__init__(self, directed=True)
        Init_Problem.__str__(self)

    def bidirectional(self, start, goal, count):
        found, fringe1, visited1, came_from1 =\
            False, deque([start]), set([start]), {start: None}
        meet, fringe2, visited2, came_from2 =\
            None, deque([goal]), set([goal]), {goal: None}

        while not found and (len(fringe1) or len(fringe2)):
            if len(fringe1):
                current1 = fringe1.pop()
                if current1 in visited2:
                    meet = current1
                    found = True
                    break
                for node in self.neighbors(current1):
                    if node not in visited1:
                        visited1.add(node)
                        fringe1.appendleft(node)
                        came_from1[node] = current1
                        count = count + 1
            if len(fringe2):
                current2 = fringe2.pop()
                if current2 in visited1:
                    meet = current2
                    found = True
                    break
                for node in self.neighbors(current2):
                    if node not in visited2:
                        visited2.add(node)
                        fringe2.appendleft(node)
                        came_from2[node] = current2
                        count = count + 1
        if found:
            return came_from1, came_from2, meet, count
        else:
            print('No path between {} and {}'.format(start, goal))
            return None, None, None, count


graph = Bidirectional()
graph.create_graph_bidirectional()
start, goal, count = 'A', 'Z', 0
trace1, trace2, meet, count = graph.bidirectional(start, goal, count)

if meet:
    print('Meeting Node:', meet)
    print('Path From Start:', end=' ')
    graph.print_path(trace1, meet)
    print('\nPath From Goal:', end=' ')
    graph.print_path(trace2, meet)
    print('\nCount:', count)