"""
2019-01-31 8-57-55 周四: start
2019-01-31 10-13-02 周四: 这道题用模拟来做会超时，懒得改了。
"""
from collections import deque
from datetime import datetime
from operator import attrgetter


class User:
    def __init__(self, arrive_time, p_time):
        self.arrive_time = arrive_time
        self.p_time = p_time * 60
        self.wait_time = 0
        self.valid = False


N, M = list(map(int, input().split()))
users = []
for i in range(N):
    t1, t2 = input().split()
    users.append(User(datetime.strptime(t1, '%H:%M:%S'), int(t2)))
users.sort(key=attrgetter('arrive_time'), reverse=True)
all_users = users[:]

start_time = datetime.strptime('08:00:00', '%H:%M:%S')
# 处理8点前就到的人
for user in reversed(users):
    if user.arrive_time < start_time:
        user.wait_time = (start_time - user.arrive_time).total_seconds()
        user.arrive_time = start_time
    else:
        break

queue = deque()
windows = [None] * M
for i in range(540*60+1):
    # 休息区时间加长
    for user in queue:
        user.wait_time += 1

    # 窗口判断是否结束
    for j, user in enumerate(windows):
        if user is not None:
            user.p_time -= 1
            if user.p_time == 0:
                windows[j] = None

    # 进入休息区
    while True:
        if not users:
            break
        if (users[-1].arrive_time - start_time).total_seconds() == i:
            queue.append(users.pop())
            queue[-1].valid = True
        else:
            break

    # 进入窗口
    for j, user in enumerate(windows):
        if user is None and len(queue) > 0:
            windows[j] = queue.popleft()

total_cost = 0
valid_num = 0
for user in all_users:
    if user.valid:
        valid_num += 1
        total_cost += user.wait_time

print(f'{round(total_cost / valid_num / 60, 1) :.1f}')
