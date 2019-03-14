N, b = list(map(int, input().split()))
items = []
if N != 0:
    while True:
        items.append(N % b)
        N //= b
        if N == 1:
            items.append(1)
            break
        elif N == 0:
            break
else:
    items.append(0)

flag = True
for i in range(len(items)):
    if items[i] != items[-(i+1)]:
        flag = False
        break
if flag:
    print('Yes')
else:
    print('No')

print(' '.join(list(map(str, reversed(items)))))
