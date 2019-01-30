"""
2019-01-30 17-58-48 周三: start
2019-01-30 18-23-09 周三: finish，注意2是素数
"""


def is_prime(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2, int(x ** 0.5 + 1)):
            if x % i == 0:
                return False
        return True


def transfer(N, D):
    ND = []
    while True:
        ND.append(N % D)
        N //= D
        if N == 1:
            ND.append(1)
            break
        elif N == 0:
            break
    real_nd = 0
    for i, each in enumerate(ND, 1):
        real_nd += each * D ** (len(ND) - i)
    return real_nd


while True:
    line = input().split()
    if len(line) == 1:
        exit(0)
    N, D = [int(each) for each in line]

    if not is_prime(N):
        print('No')
    else:
        ND = transfer(N, D)
        if is_prime(ND):
            print('Yes')
        else:
            print('No')
