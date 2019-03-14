"""
start time: 2019年2月20日23:32:53
放弃，我宁可用c++做模拟，也不会再尝试用python来推排队了
"""
from collections import deque
from copy import copy
from datetime import datetime, timedelta

flag_time = datetime.strptime("22:00:00", "%H:%M:%S")


class Person:
    def __init__(self, arrive_time, play_time, vip):
        self.arrive_time = datetime.strptime(arrive_time, "%H:%M:%S")
        self.play_time = play_time if play_time < 120 else 120
        self.serve_time = flag_time
        self.vip = vip == "1"


class Table:
    def __init__(self, id1):
        self.id1 = id1
        self.vip = False
        self.finish_time = None
        self.free = True
        self.counter = 0


def update_table(tables, time_now):
    has_table_free = False
    for table in tables:
        if not table.free and table.finish_time <= time_now:
            table.free = True
            has_table_free = True
            break
        elif table.free:
            has_table_free = True
            break
    return has_table_free


def update_people(people, queue, time_now):
    while True:
        if people != [] and people[-1].arrive_time <= time_now:
            queue.append(people.pop())
        else:
            break


def find_vip(queue):
    for person in queue:
        if person.vip:
            return person
    return None


n = int(input())
people = []

for i in range(n):
    arrive_time, play_time, vip = input().split()
    people.append(Person(arrive_time, int(play_time), vip))
people.sort(key=lambda x: x.arrive_time, reverse=True)
people1 = copy(people)

table_number, vip_table_number = list(map(int, input().split()))
tables = [Table(i) for i in range(1, table_number + 1)]
v_table_indexes = list(map(int, input().split()))
for idx in v_table_indexes:
    tables[idx-1].vip = True

time_now = datetime.strptime("08:00:00", "%H:%M:%S")
end_time = datetime.strptime("21:00:00", "%H:%M:%S")
queue = deque()
while True:
    if people == [] or time_now >= end_time:
        break

    has_table_free = update_table(tables, time_now)

    if not has_table_free:
        time_now = tables[0].finish_time
        for table in tables:
            if time_now > table.finish_time:
                time_now = table.finish_time
        continue

    update_people(people, queue, time_now)
    if len(queue) > 0:
        vip_user = find_vip(queue)
        if vip_user is not None:
            # 这里find_vip函数直接重用了
            vip_table = find_vip(tables)
            if vip_table is not None:
                queue.remove(vip_user)
                vip_user.serve_time = time_now
                vip_table.free = False
                vip_table.counter += 1
                vip_table.finish_time = time_now + timedelta(minutes=vip_user.play_time)
                continue
        else:
            process_table = None
            for table in tables:
                if table.free:
                    process_table = table
                    break
            queue[-1].serve_time = time_now
            process_table.free = False
            process_table.counter += 1
            process_table.finish_time = time_now + timedelta(minutes=queue[-1].play_time)
            queue.popleft()
    else:
        queue.append(people.pop())
        time_now = queue[0].arrive_time
        continue

people1.sort(key=lambda x: x.serve_time)
for person in people1:
    if person.serve_time != flag_time:
        wait_time = (person.serve_time - person.arrive_time).total_seconds() // 60
        if (person.serve_time - person.arrive_time).total_seconds() % 60 >= 30:
            wait_time += 1
        print(f"{person.arrive_time.strftime('%H:%M:%S')} {person.serve_time.strftime('%H:%M:%S')} {wait_time:.0f}")
counters = [str(table.counter) for table in tables]
print(" ".join(counters))

"""
    # 有没有桌子空
        # 如果有桌子空，看看queue里有没有人
            # 如果有人，看看这些人里面有没有vip用户
                # 如果有vip用户，看看有没有vip桌子空
                    # 如果有，就分配给他
            # 如果没有vip用户，那就正常按顺序给他们分配，先来的人得到id最小的桌子
        # 如果queue里没有人，那就看最先到达的人是谁
        # 看看根据这个人到达的时间，是不是有更多的桌子空出来了
        # 看看这个人是不是vip，看看有没有vip桌子空出来恰好给他
            # 如果没有，就正常给他分配id最小的桌子
"""
