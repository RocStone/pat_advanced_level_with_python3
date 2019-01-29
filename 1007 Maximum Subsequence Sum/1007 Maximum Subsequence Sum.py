
K = int(input())
seq = [int(each) for each in input().split()]
i = cur_i = 0
j = cur_j = len(seq) - 1
max_sum = 0
cur_sum = 0
for index, each in enumerate(seq):
    if each + cur_sum < 0:
        cur_i = index + 1
        cur_sum = 0
    elif each + cur_sum >= 0:
        cur_sum += each
        cur_j = index
        if cur_sum > max_sum:
            max_sum = cur_sum
            i = cur_i
            j = cur_j
# 单独处理和为0，但是由单个0组成的情况，例如输入为-1 0 -1，输出应该是0 1 1
if max_sum == 0:
    for index, each in enumerate(seq):
        if each == 0:
            i = j = index
            break
print(f'{max_sum} {seq[i]} {seq[j]}')

