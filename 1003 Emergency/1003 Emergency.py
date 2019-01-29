from math import inf


class Edge:
    def __init__(self, a, b, weight):
        self.a = a
        self.b = b
        self.weight = weight


class Node:
    def __init__(self, no):
        self.no = no
        self.edges = []
        self.parents = []
        self.visited = False
        self.dist = inf

    def add_edge(self, a, b, weight):
        self.edges.append(Edge(a, b, weight))


def find_nearest(nodes):
    min_dist = inf
    min_node = None
    for node in nodes:
        if not node.visited and node.dist < min_dist:
            min_dist = node.dist
            min_node = node
    min_node.visited = True
    return min_node


def relax_neighbors(min_node, nodes):
    for edge in min_node.edges:
        v = nodes[edge.b]
        if v.dist > min_node.dist + edge.weight:
            v.parents = [min_node]
            v.dist = min_node.dist + edge.weight
        elif v.dist == min_node.dist + edge.weight:
            v.parents.append(min_node)


def dfs(cur_node, number):
    global max_number, diff_ways
    number += teams[cur_node.no]
    if cur_node == nodes[c1]:
        if max_number < number:
            max_number = number
        diff_ways += 1
        return
    for node in cur_node.parents:
        dfs(node, number)


N, M, c1, c2 = [int(item) for item in input().split()]
teams = [int(item) for item in input().split()]
nodes = [Node(i) for i in range(N)]
for i in range(M):
    a, b, weight = [int(item) for item in input().split()]
    nodes[a].add_edge(a, b, weight)
    nodes[b].add_edge(b, a, weight)

# Dijkstra
nodes[c1].dist = 0
while True:
    min_node = find_nearest(nodes)
    if min_node.no == c2:
        break
    relax_neighbors(min_node, nodes)


# calc teams
max_number = 0
diff_ways = 0
dfs(nodes[c2], teams[c2])
print(f'{diff_ways} {max_number-teams[c2]}')
