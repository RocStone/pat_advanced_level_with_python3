"""
start time: 2019-02-22 15-36-15 周五
坑： 超时，直接不用想了，c++吧
end time: 2019-02-22 15-42-40 周五
"""
from collections import defaultdict

N, K = list(map(int, input().split()))
course = defaultdict(list)
for i in range(K):
    no, _ = list(map(int, input().split()))
    students = input().split()
    for student in students:
        course[student].append(no)

q_students = input().split()
for student in q_students:
    print(f"{student} {len(course[student])}", end="")
    for each_course in sorted(course[student]):
        print(f" {each_course}", end="")
    print()


