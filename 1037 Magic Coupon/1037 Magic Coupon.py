"""
start time: 2019-02-22 14-30-02 周五
end time: 2019-02-22 14-46-01 周五
"""


n1 = int(input())
list1 = list(map(int, input().split()))
n2 = int(input())
list2 = list(map(int, input().split()))

list1.sort(reverse=True)
list2.sort(reverse=True)
list1_n, list1_p, list2_n, list2_p = [], [], [], []

for each in list1:
    if each < 0:
        list1_n.append(each)
    elif each > 0:
        list1_p.append(each)
for each in list2:
    if each < 0:
        list2_n.append(each)
    elif each > 0:
        list2_p.append(each)

total_sum = 0

for x, y in zip(reversed(list1_n), reversed(list2_n)):
    if x * y > 0:
        total_sum += x * y

for x, y in zip(list1_p, list2_p):
    if x * y > 0:
        total_sum += x * y

print(total_sum)
