"""
start time: 2019-02-22 13-57-11 周五
end time: 2019-02-22 14-05-57 周五
"""


class User:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.modified = False
        self.check_code()

    def check_code(self):
        new_code = []
        for alpha in self.code:
            if alpha == '1':
                self.modified = True
                new_code.append('@')
            elif alpha == '0':
                self.modified = True
                new_code.append('%')
            elif alpha == 'l':
                self.modified = True
                new_code.append('L')
            elif alpha == 'O':
                self.modified = True
                new_code.append('o')
            else:
                new_code.append(alpha)
        self.code = ''.join(new_code)


n = int(input())
users = []
for i in range(n):
    name, code = input().split()
    users.append(User(name, code))

modified_number = 0
modified_users = []
for user in users:
    if user.modified:
        modified_number += 1
        modified_users.append(user)


if modified_number > 0:
    print(modified_number)
    for user in modified_users:
        print(f"{user.name} {user.code}")
elif len(users) == 1:
    print("There is 1 account and no account is modified")
else:
    print(f"There are {len(users)} accounts and no account is modified")


