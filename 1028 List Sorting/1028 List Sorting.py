"""
start time:2019年2月21日14:55:33
end time: 2019年2月21日15:14:46
坑: 最后一个测试点读取就超时，要用c++来做
"""


class Student:
    def __init__(self, no, name, score):
        self.str_no = no
        self.no = int(no)
        self.name = name
        self.score = int(score)


N, C = list(map(int, input().split()))
students = []
for i in range(N):
    no, name, score = input().split()
    students.append(Student(no, name, score))

if C == 1:
    students.sort(key=lambda x: x.no)
elif C == 2:
    students.sort(key=lambda x: (x.name, x.no))
elif C == 3:
    students.sort(key=lambda x: (x.score, x.no))

for student in students:
    print(f'{student.str_no} {student.name} {student.score}')


