'''
Given information about active users on the network, find the shortest
route for a message from one user (the sender) to another (the recipient).
Return a list of users that make up this route.

Takeaways:
    1) Know BFS and DFS like the back of your hand.
    2) Backtracking requires you to store the previous nodes!!
'''

from collections import deque

# O(n + m) time, where n is number of nodes in the graph m is the number of edges * 2
# O(n) space for storing dictionary of previous node
def find_shortest_path(graph, start, end):
    if start not in graph or end not in graph:
        raise Exception('Need start and end nodes to be in graph')

    queue = deque([start])
    previous_node = {start:None}
    while queue:
        current_node = queue.popleft()
        if current_node == end:
            return backtrace(previous_node, end)
        for neighbor in graph[current_node]:
            if neighbor not in previous_node:
                previous_node[neighbor] = current_node
                queue.append(neighbor)
    return None

def backtrace(previous_node, end):
    backtrace = []
    curr_node = end
    while curr_node:
        backtrace.append(curr_node)
        curr_node = previous_node[curr_node]
    return list(reversed(backtrace))

graph = {
    'Min'     : ['William', 'Jayden', 'Omar'],
    'William' : ['Min', 'Noam'],
    'Jayden'  : ['Min', 'Amelia', 'Ren', 'Noam'],
    'Ren'     : ['Jayden', 'Omar'],
    'Amelia'  : ['Jayden', 'Adam', 'Miguel'],
    'Adam'    : ['Amelia', 'Miguel', 'Sofia', 'Lucas'],
    'Miguel'  : ['Amelia', 'Adam', 'Liam', 'Nathan'],
    'Noam'    : ['Nathan', 'Jayden', 'William'],
    'Omar'    : ['Ren', 'Min', 'Scott'],
}

print(find_shortest_path(graph, 'Jayden', 'Adam'))
