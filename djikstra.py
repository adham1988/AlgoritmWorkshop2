from collections import defaultdict
import time



listofnodes = []
class Graph():
    def __init__(self):
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.weights = {}

    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight
        listofnodes.append(to_node)



graph = Graph()

edges = [
    ('X', 'A', 7),
    ('X', 'B', 2),
    ('X', 'C', 3),
    ('X', 'E', 4),
    ('A', 'B', 3),
    ('A', 'D', 4),
    ('B', 'D', 4),
    ('B', 'H', 5),
    ('C', 'L', 2),
    ('D', 'F', 1),
    ('F', 'H', 3),
    ('G', 'H', 2),
    ('G', 'Y', 2),
    ('I', 'J', 6),
    ('I', 'K', 4),
    ('I', 'L', 4),
    ('J', 'L', 1),
    ('K', 'Y', 5),
]
"""
edges = [
    ('X', 'A', 7),
    ('X', 'B', 2),
    ('X', 'C', 8),
    ('X', 'E', 4),
    ('A', 'D', 2),
    ('D', 'G', 9),
    ('B', 'G', 3),
    ('E', 'F', 7),
    ('F', 'G', 7),
    ('G', 'H', 4),
    ('G', 'I', 6),
    ('H', 'J', 8),
    ('I', 'J', 7),
]
"""""
for edge in edges:
    graph.add_edge(*edge)
listofnodes = list(dict.fromkeys(listofnodes))
print("list of unvisited nodes",listofnodes)
start_time = time.time()
def dijsktra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    print("")
    print("first block: current node",current_node)
    visited = set()
    print("")
    while current_node != end:
        visited.add(current_node)
        print("current node", current_node)
        destinations = graph.edges[current_node]
        print("destination options from ", current_node,"are : ",destinations)
        weight_to_current_node = shortest_paths[current_node][1]
        print("weight to current node", weight_to_current_node)

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        print("after relaxation ",shortest_paths)
        print("add",current_node,"to the visited list")
        print("visited list :", visited)
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            print("no possible routes")
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

        print("")
        print("")
    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
        print("Work back through destinations in shortest path",current_node)
    # Reverse path
    path = path[::-1]
    print("")
    print("")
    print(*path, sep = " -> ")
    return path


dijsktra(graph, 'X', 'J')
print("execution time = --- %s ms ---" % ((time.time() - start_time)*1000))

print("the time complexity in this case is O(E+VlogV)")