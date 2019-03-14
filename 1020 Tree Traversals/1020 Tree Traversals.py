from collections import deque


def find_root(pleft, pright, inleft, inright):
    global inorder, post
    for j in range(pright, pleft - 1, -1):
        for i in range(inleft, inright + 1):
            if post[j] == inorder[i]:
                return j, i
    return -1, -1


N = int(input())
post = list(map(int, input().split()))
inorder = list(map(int, input().split()))

level = []
queue = deque()
queue.append([0, N - 1, 0, N - 1])
while len(queue) > 0:
    left_post, right_post, left_in, right_in = queue.popleft()
    root_post, root_in = find_root(left_post, right_post, left_in, right_in)
    if root_post == -1:
        continue
    level.append(post[root_post])
    left_len = root_in - left_in
    right_len = right_in - root_in
    if left_post == root_post:
        left_post += 1
    queue.append([left_post, left_post + left_len - 1, left_in, root_in - 1])
    if left_post + left_len == root_post:
        left_post += 1

    queue.append([left_post + left_len, left_post + left_len + right_len - 1, root_in + 1, right_in])

print(' '.join(list(map(str, level))))
