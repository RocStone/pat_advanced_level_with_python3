"""
start time: 2019年2月20日22:45:23
end time: 2019年2月20日23:17:05
坑：这道题用python做最后一个测试点会超时，用c++重写下就好了，懒得写了跳过吧
"""


class Person:
    def __init__(self, id1, score, local_number):
        self.id1 = id1
        self.local_rank = -1
        self.final_rank = -1
        self.score = score
        self.local_number = local_number


n = int(input())
people = []
for i in range(n):
    k = int(input())
    local = []
    for j in range(k):
        raw = input().split()
        id1 = raw[0]
        score = int(raw[1])
        person = Person(id1, score, i+1)
        local.append(person)
        people.append(person)
    # 当地排序也很麻烦
    local.sort(key=lambda x: (-x.score, x.id1))
    last_rank = 0
    last_score = -1
    for i, person in enumerate(local, 1):
        if person.score == last_score:
            person.local_rank = last_rank
        else:
            person.local_rank = i
            last_rank = i
            last_score = person.score

people.sort(key=lambda x: (-x.score, x.id1))
last_rank = 0
last_score = -1
for i, person in enumerate(people, 1):
    if person.score == last_score:
        person.final_rank = last_rank
    else:
        person.final_rank = i
        last_rank = i
        last_score = person.score

print(len(people))
for person in people:
    print(f"{person.id1} {person.final_rank} {person.local_number} {person.local_rank}")
