
def visit_dfs(root):
    visited[root] = True
    for v in edges[root]:
        if not visited[v]:
            visit_dfs(v)


def most_far(root):
    depth, node = 0, [root]
    visited[root] = True
    for each in edges[root]:
        if not visited[each]:
            d, nd = most_far(each)
            if d > depth:
                depth = d
                node = nd
            elif d == depth:
                node.extend(nd)
    return depth + 1, node


N = int(input())
u, v = 0, 0
edges = [[] for i in range(N + 1)]
for i in range(N - 1):
    u, v = list(map(int, input().split()))
    edges[u].append(v)
    edges[v].append(u)

components = 0
visited = [False for i in range(N + 1)]
for i in range(1, N + 1):
    if not visited[i]:
        components += 1
        visit_dfs(i)
if components != 1:
    print('Error: {} components'.format(components))
    exit(0)

visited = [False for i in range(N + 1)]
_, far_nodes = most_far(u)
result = set(far_nodes)

visited = [False for i in range(N + 1)]
_, far_nodes = most_far(far_nodes[0])
result = result.union(far_nodes)
result = list(result)
result.sort()
for each in result:
    print(each)


