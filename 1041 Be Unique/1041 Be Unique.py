"""
start time: 2019-02-26 11-55-52 周二
end time: 2019-02-26 11-59-36 周二
"""

count = [0] * 10001
_, *bets = list(map(int, input().split()))
for each in bets:
    count[each] += 1

for each in bets:
    if count[each] == 1:
        print(each)
        exit(0)
print('None')
