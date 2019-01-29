def dfs(node, level):
    global children, leaves, max_level
    for child in children[node]:
        dfs(child, level + 1)
    if not children[node]:
        leaves[level] += 1
        if level > max_level:
            max_level = level


children = [[] for i in range(100)]
leaves = [0] * 100
max_level = 0
N, M = [int(each) for each in input().split()]
for i in range(M):
    no, k, *children_no = [int(each) for each in input().split()]
    children[no] = children_no
dfs(1, 0)
str_leaves = [str(each) for each in leaves]
print(' '.join(str_leaves[:max_level + 1]))
