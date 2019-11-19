import networkx as nx
from networkx.algorithms.flow import edmonds_karp 
import matplotlib.pyplot as plt
import datetime


def draw_graph():
    plt.figure(figsize=(12, 4))
    plt.axis('off')

    nx.draw_networkx_nodes(graph, layout, node_color='steelblue', node_size=450)
    nx.draw_networkx_edges(graph, layout, edge_color='black')
    nx.draw_networkx_labels(graph, layout, font_color='white')

    for u, v, e in graph.edges(data=True):
        label = '{}/{}'.format(e['flow'], e['capacity'])
        color = 'green' if e['flow'] <= e['capacity'] else 'red'
        x = layout[u][0] * .6 + layout[v][0] * .4
        y = layout[u][1] * .6 + layout[v][1] * .4
        t = plt.text(x, y, label, size=16, color=color, 
                     horizontalalignment='center', verticalalignment='center')
    plt.show()

def ford_fulkerson(graph, source, sink):
    flow, path = 0, True
    
    while path:
        # search for path with flow reserve
        path, reserve = depth_first_search(graph, source, sink)
        flow += reserve

        # increase flow along the path
        for v, u in zip(path, path[1:]):
            if graph.has_edge(v, u):
                graph[v][u]['flow'] += reserve
            else:
                graph[u][v]['flow'] -= reserve

def depth_first_search(graph, source, sink):
    undirected = graph.to_undirected()
    explored = {source}
    stack = [(source, 0, dict(undirected[source]))]
    
    while stack:
        v, _, neighbours = stack[-1]
        if v == sink:
            break
        
        # search the next neighbour
        while neighbours:
            u, e = neighbours.popitem()
            if u not in explored:
                break
        else:
            stack.pop()
            continue
        
        # current flow and capacity
        in_direction = graph.has_edge(v, u)
        capacity = e['capacity']
        flow = e['flow']
        neighbours = dict(undirected[u])

        # increase or redirect flow at the edge
        if in_direction and flow < capacity:
            stack.append((u, capacity - flow, neighbours))
            explored.add(u)
        elif not in_direction and flow:
            stack.append((u, flow, neighbours))
            explored.add(u)

    # (source, sink) path and its flow reserve
    reserve = min((f for _, f, _ in stack[1:]), default=0)
    path = [v for v, _, _ in stack]
    
    return path, reserve

graph = nx.DiGraph()
graph.add_nodes_from('SABCDZ')
graph.add_edges_from([
    ('S', 'A', {'capacity': 10, 'flow': 0}),
    ('S', 'C', {'capacity': 10, 'flow': 0}),
    ('A', 'C', {'capacity': 2, 'flow': 0}),
    ('A', 'B', {'capacity': 4, 'flow': 0}),
    ('A', 'D', {'capacity': 8, 'flow': 0}),
    ('B', 'Z', {'capacity': 10, 'flow': 0}),
    ('C', 'D', {'capacity': 9, 'flow': 0}),
    ('D', 'B', {'capacity': 6, 'flow': 0}),
    ('D', 'Z', {'capacity': 10, 'flow': 0}),
])

biggraph = nx.DiGraph()
biggraph.add_nodes_from('SABCDZ')
biggraph.add_edges_from([
    ('S', 'A', {'capacity': 10, 'flow': 0}),
    ('S', 'B', {'capacity': 10, 'flow': 0}),
    ('S', 'C', {'capacity': 2, 'flow': 0}),
    ('S', 'D', {'capacity': 4, 'flow': 0}),
    ('S', 'E', {'capacity': 8, 'flow': 0}),
    ('A', 'S', {'capacity': 10, 'flow': 0}),
    ('A', 'B', {'capacity': 9, 'flow': 0}),
    ('A', 'C', {'capacity': 6, 'flow': 0}),
    ('A', 'D', {'capacity': 10, 'flow': 0}),
    ('A', 'E', {'capacity': 10, 'flow': 0}),
    ('B', 'S', {'capacity': 10, 'flow': 0}),
    ('B', 'A', {'capacity': 2, 'flow': 0}),
    ('B', 'C', {'capacity': 4, 'flow': 0}),
    ('B', 'D', {'capacity': 8, 'flow': 0}),
    ('B', 'E', {'capacity': 10, 'flow': 0}),
    ('C', 'S', {'capacity': 9, 'flow': 0}),
    ('C', 'A', {'capacity': 6, 'flow': 0}),
    ('C', 'B', {'capacity': 10, 'flow': 0}),
    ('C', 'D', {'capacity': 10, 'flow': 0}),
    ('C', 'E', {'capacity': 10, 'flow': 0}),
    ('D', 'S', {'capacity': 2, 'flow': 0}),
    ('D', 'A', {'capacity': 4, 'flow': 0}),
    ('D', 'B', {'capacity': 8, 'flow': 0}),
    ('D', 'C', {'capacity': 10, 'flow': 0}),
    ('D', 'E', {'capacity': 9, 'flow': 0}),
    ('E', 'S', {'capacity': 6, 'flow': 0}),
    ('E', 'A', {'capacity': 10, 'flow': 0}),
    ('E', 'B', {'capacity': 10, 'flow': 0}),
    ('E', 'C', {'capacity': 10, 'flow': 0}),
    ('E', 'D', {'capacity': 2, 'flow': 0}),
    ('E', 'Z', {'capacity': 2, 'flow': 0}),
])

layout = {
    'S': [0, 1], 
    'A': [1, 2], 
    'B': [2, 2], 
    'C': [1, 0],
    'D': [2, 0], 
    'Q': [3, 2],
    'Z': [3, 1],
}
before = datetime.datetime.now()
ford_fulkerson(graph, 'S', 'Z')
after = datetime.datetime.now()
time = after - before

print(time)
#draw_graph()



G = nx.DiGraph()
G.add_edge('S','A', capacity=10.0)
G.add_edge('S','C', capacity=10.0)
G.add_edge('A','C', capacity=2.0)
G.add_edge('A','B', capacity=4.0)
G.add_edge('A','D', capacity=8.0)
G.add_edge('B','Z', capacity=10.0)
G.add_edge('C','D', capacity=9.0)
G.add_edge('D','B', capacity=6.0)
G.add_edge('D','Z', capacity=10.0)


before = datetime.datetime.now()
R = edmonds_karp(G, 'S','Z')
after = datetime.datetime.now()
time = after - before
print(time)
flow_value = nx.maximum_flow_value(G, 'S', 'Z')
flow_value
3.0
flow_value == R.graph['flow_value']
True
print(flow_value)