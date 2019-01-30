"""
坑：分数相同的情况，排名应该是1 2 2 2 5 6，而不是1 2 2 2 3 4
"""


from operator import attrgetter


class Student:
    def __init__(self, no, c, m, e):
        self.no = no
        self.c = c
        self.m = m
        self.e = e
        self.a = round((c + m + e) / 3, 0)
        self.ra = 0
        self.rc = 0
        self.rm = 0
        self.re = 0

    def print_result(self):
        tmp = [self.ra, self.rc, self.re, self.rm]
        min_tmp = min(tmp)
        if min_tmp == self.ra:
            print(f'{self.ra} A')
        elif min_tmp == self.rc:
            print(f'{self.rc} C')
        elif min_tmp == self.rm:
            print(f'{self.rm} M')
        else:
            print(f'{self.re} E')


students = []
students_dict = dict()

N, M = [int(each) for each in input().split()]
for i in range(N):
    line = input().split()
    s = Student(line[0].strip(), int(line[1]), int(line[2]), int(line[3]))
    students.append(s)
    students_dict[line[0].strip()] = s

check_list = []
for i in range(M):
    each = input().strip()
    check_list.append(each)

# 按照四种进行排序
students.sort(key=attrgetter('a'), reverse=True)
rank = 0
last_value = -1
for i, student in enumerate(students, 1):
    if student.a != last_value:
        last_value = student.a
        student.ra = i
        rank = i
    else:
        student.ra = rank

students.sort(key=attrgetter('c'), reverse=True)
rank = 0
last_value = -1
for i, student in enumerate(students, 1):
    if student.c != last_value:
        last_value = student.c
        student.rc = i
        rank = i
    else:
        student.rc = rank

students.sort(key=attrgetter('m'), reverse=True)
rank = 0
last_value = -1
for i, student in enumerate(students, 1):
    if student.m != last_value:
        last_value = student.m
        student.rm = i
        rank = i
    else:
        student.rm = rank

students.sort(key=attrgetter('e'), reverse=True)
rank = 0
last_value = -1
for i, student in enumerate(students, 1):
    if student.e != last_value:
        last_value = student.e
        student.re = i
        rank = i
    else:
        student.re = rank

# 输出结果
for student_no in check_list:
    if student_no not in students_dict.keys():
        print('N/A')
    else:
        students_dict[student_no].print_result()
