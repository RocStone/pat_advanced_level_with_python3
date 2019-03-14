from math import inf


class Edge:
    def __init__(self, u, v, length):
        self.u = u
        self.v = v
        self.length = length


def find_nearest():
    global visited, dist, N
    min_dist = inf
    index = -1
    for i in range(N + 1):
        if not visited[i] and dist[i] < min_dist:
            min_dist = dist[i]
            index = i
    return index


def dijkstra():
    global visited, edges, dist, parents
    while True:
        index = find_nearest()
        if index == SP:
            break
        else:
            # 更新附近所有站点
            visited[index] = True
            for edge in edges[index]:
                if not visited[edge.v]:
                    if dist[edge.v] > dist[index] + edge.length:
                        dist[edge.v] = dist[index] + edge.length
                        parents[edge.v] = [index]
                    elif dist[edge.v] == dist[index] + edge.length:
                        parents[edge.v].append(index)


stack, min_remain, min_out_bikes, min_route = [], inf, inf, []


def dfs(index):
    global stack
    if index == 0:
        remain, out_bikes = 0, 0
        for i in reversed(stack):
            if bikes[i] > Capacity / 2:
                remain += bikes[i] - Capacity / 2
            elif bikes[i] < Capacity / 2:
                remain -= Capacity / 2 - bikes[i]
                if remain < 0:
                    out_bikes -= remain
                    remain = 0
        global min_remain, min_out_bikes, min_route
        if min_out_bikes > out_bikes or min_out_bikes == out_bikes and min_remain > remain:
            min_out_bikes = out_bikes
            min_remain = remain
            min_route = [0]
            min_route.extend(stack[::-1])
    else:
        stack.append(index)
        for p in parents[index]:
            dfs(p)
        stack.pop()


Capacity, N, SP, M = list(map(int, input().split()))
bikes = [0]
bikes.extend(list(map(int, input().split())))
edges = [[] for i in range(N + 1)]
for i in range(M):
    u, v, length = list(map(int, input().split()))
    edges[u].append(Edge(u, v, length))
    edges[v].append(Edge(v, u, length))

dist = [inf] *(N + 1)
dist[0] = 0
visited = [False for i in range((N + 1))]
parents = [[] for i in range(N + 1)]
dijkstra()
dfs(SP)
print(f'{min_out_bikes:.0f} {"->".join(map(str, min_route))} {min_remain:.0f}')
