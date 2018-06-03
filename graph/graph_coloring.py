'''
Given an undirected graph with maximum degree D,
Find a graph coloring using at most D + 1 colors.

Degree: The number of edges connected to a node
Graph coloring:
    Assign colors to nodes in a graph.
    A legal coloring means no adjacent nodes can have the same color


Takeaways:
    1) Represent graph problem time costs in vertices and edges.
    2) Consider graph edge cases like loops, cycles, and single nodes.
'''

class GraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None

# O(N + M) time, where N is the number of nodes and M the number of edges.
# O(D) space, where D is the max degree of the graph
def color_graph(nodes, colors):
    for node in nodes:
        if not node.neighbors or node in node.neighbors:
            raise Exception('You cannot add any loops or single nodes in the graph!')
        illegal_colorings = set([neighbor.color for neighbor in node.neighbors if node.neighbors])
        for color in colors:
            if color not in illegal_colorings:
                node.color = color
                break

a = GraphNode('a')
b = GraphNode('b')
c = GraphNode('c')

a.neighbors.add(b)
b.neighbors.add(a)
b.neighbors.add(c)
c.neighbors.add(b)

graph = [a, b, c]
colors = ['red', 'green', 'blue']
color_graph(graph, colors)
for node in graph:
    print('Label: {}, Color: {}'.format(node.label, node.color))
