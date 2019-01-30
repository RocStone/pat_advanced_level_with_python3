"""
2019-01-30 14-07-33 周三：start
2019-01-30 14-31-55 周三: one case run time over, consider about using a stack to implement dfs
2019-01-30 14-37-49 周三：still run time over, consider don't add a node to stack if visited
2019-01-30 14-39-16 周三: still run time over, consider about using a set to implement stack
2019-01-30 14-41-59 周三: still run time over
2019-01-30 15-00-22 周三: the problem is not dfs, it's M being too large
2019-01-30 15-46-20 周三: the problem is python doesn't have scanf, so even map is fast, str.split() cost too much memory
                            I'll just give up, this practice should be done with c++
"""
import sys


class Node:
    __slots__ = ['no', 'connected_cities']

    def __init__(self, no):
        self.no = no
        self.connected_cities = []


N, M, K = [int(each) for each in input().split()]
# node[0] 这个节点不被使用，这样可以从1开始数
nodes = [Node(i) for i in range(N + 1)]
lines = sys.stdin.read()
numbers = list(map(int, lines.split()))
for i in range(M):
    u, v = numbers[i * 2], numbers[i * 2 + 1]
    nodes[u].connected_cities.append(v)
    nodes[v].connected_cities.append(u)

check_list = numbers[2 * M:]


def dfs(i, lost_city):
    global visited, nodes
    stack = set()
    stack.add(nodes[i])
    while stack:
        node = stack.pop()
        if visited[node.no]:
            continue
        visited[node.no] = True
        for each_city in node.connected_cities:
            if each_city != lost_city and not visited[each_city]:
                stack.add(nodes[each_city])


for lost_city in check_list:
    visited = [False] * (N + 1)
    repair_highways = -1
    for i in range(1, N + 1):
        if not visited[i] and i != lost_city:
            dfs(i, lost_city)
            repair_highways += 1
    print(repair_highways)
