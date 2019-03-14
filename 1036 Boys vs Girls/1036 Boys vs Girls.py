"""
start time: 2019-02-22 14-11-15 周五
end time: 2019-02-22 14-24-20 周五
"""


class Student:
    def __init__(self, name, gender, score, course):
        self.name = name
        self.gender = gender
        self.score = int(score)
        self.course = course


n = int(input())
f_students = []
m_students = []
for i in range(n):
    name, gender, course, score = input().split()
    if gender == 'M':
        m_students.append(Student(name, gender, score, course))
    else:
        f_students.append(Student(name, gender, score, course))

if f_students:
    female_top = max(f_students, key=lambda x: x.score)
    print(f"{female_top.name} {female_top.course}")
else:
    print('Absent')

if m_students:
    male_end = min(m_students, key=lambda x: x.score)
    print(f"{male_end.name} {male_end.course}")
else:
    print('Absent')


if f_students and m_students:
    print(f"{female_top.score - male_end.score}")
else:
    print('NA')

