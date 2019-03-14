"""
start time: 2019-02-26 15-13-50 周二

坑：又TM的超时，又要C++
"""

N = int(input())
f_color_length, *f_color = list(map(int, input().split()))
_, *strip = list(map(int, input().split()))

order = dict()                      # 记录该颜色的优先级，方便一会查找
for i, each in enumerate(f_color):
    order[each] = i

last_length = dict()              # 为了使用该颜色，目前能得到的最长长度
for each in f_color:
    last_length[each] = 0

for color in strip:
    # 所以优先级低于该颜色的color，长度都可以加1
    if color in order:
        pre_max_length = 0
        o = order[color]
        for i in range(0, o + 1):
            if last_length[f_color[i]] > pre_max_length:
                pre_max_length = last_length[f_color[i]]
        last_length[color] = pre_max_length + 1
        for i in range(o + 1, f_color_length):
            if last_length[color] > last_length[f_color[i]]:
                last_length[f_color[i]] = last_length[color]

max_length = 0
for each in last_length.values():
    if each > max_length:
        max_length = each
print(max_length)
