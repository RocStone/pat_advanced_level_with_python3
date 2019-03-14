"""
start time: 2019-02-22 13-13-42 周五
end time: 2019-02-22 13-51-18 周五
坑： 1. 注意关系是双向的，A call B时，应该在B里面也添加A call B这个记录，否则在例子1中，C就没有与之相关的人了
    2. 关系双向添加后，注意整个gang的时间都变双倍了，因为 A call B一条记录在A和B两个人算时间的时候各自算了一次，
"""
from collections import defaultdict, deque
from math import inf


class Relate:
    def __init__(self, b, length):
        self.b = b
        self.length = length


N, K = list(map(int, input().split()))
relation = defaultdict(list)
visited = dict()
duration = defaultdict(int)
all_names = set()
for i in range(N):
    a, b, length = input().split()
    length = int(length)
    relation[a].append(Relate(b, length))
    relation[b].append(Relate(a, length))
    if a not in all_names:
        all_names.add(a)
    if b not in all_names:
        all_names.add(b)

for person in all_names:
    visited[person] = False

result = []
for each in all_names:
    if not visited[each]:
        queue = deque()
        queue.append(each)
        gang_time = 0
        gang_set = set()
        while queue:
            cur_person = queue.popleft()
            if visited[cur_person]:
                continue
            visited[cur_person] = True
            for relate in relation[cur_person]:
                queue.append(relate.b)
                duration[cur_person] += relate.length
                duration[relate.b] += relate.length
                gang_time += relate.length
                if cur_person not in gang_set:
                    gang_set.add(cur_person)
                if relate.b not in gang_set:
                    gang_set.add(relate.b)
        if len(gang_set) > 2 and gang_time / 2 > K:
            max_length = -inf
            gang_head = None
            for gang_member in gang_set:
                if duration[gang_member] > max_length:
                    max_length = duration[gang_member]
                    gang_head = gang_member
            result.append([gang_head, len(gang_set)])
print(len(result))
for each in sorted(result, key=lambda x: x[0]):
    print(f'{each[0]} {each[1]}')
