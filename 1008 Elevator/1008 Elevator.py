N, *seq = [int(each) for each in input().split()]
cur_floor = 0
total_time = 0
for each in seq:
    if cur_floor <= each:
        total_time += (each - cur_floor) * 6 + 5
    elif cur_floor > each:
        total_time += (cur_floor - each) * 4 + 5
    cur_floor = each
print(total_time)
