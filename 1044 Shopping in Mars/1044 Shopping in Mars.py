"""
坑：有一个测试点超时，虽然超时不多，但没办法优化了，用C++吧，干
"""

from math import inf



N, M = list(map(int, input().split()))

wrong_ans = []
wrong_diff = inf
right_ans = []
diamonds = list(map(int, input().split()))
ds = [0]
for i in range(len(diamonds)):
    ds.append(ds[i] + diamonds[i])

j = 0
i = 0
find_right_ans = False
length = len(ds)
while i <= j < length:
    if ds[j] - ds[i] < M:
        j += 1
    elif ds[j] - ds[i] == M:
        right_ans.append(f"{i + 1}-{j}")
        find_right_ans = True
        j += 1
        i += 1
    else:
        if not find_right_ans:
            if wrong_diff > ds[j] - ds[i]:
                wrong_ans = [f"{i + 1}-{j}"]
                wrong_diff = ds[j] - ds[i]
            elif wrong_diff == ds[j] - ds[i]:
                wrong_ans.append(f"{i + 1}-{j}")
        i += 1

if find_right_ans:
    for each in right_ans:
        print(each)
else:
    for each in wrong_ans:
        print(each)
