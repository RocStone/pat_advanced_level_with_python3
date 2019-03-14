"""
start time: 2019年2月21日14:37:54
end time: 2019年2月21日14:48:30
"""


def alpha(number):
    if number < 10:
        return number
    else:
        return chr(65 + number - 10)


def transfer(number):
    d = alpha(number // 13)
    e = alpha(number % 13)
    return "{}{}".format(d, e)


a, b, c = list(map(int, input().split()))
print(f"#{transfer(a)}{transfer(b)}{transfer(c)}")

