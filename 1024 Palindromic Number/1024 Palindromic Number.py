"""
start time: 2019年2月20日22:31:11
end time: 2019年2月20日22:44:46
"""


def is_palindromic(N):
    a = str(N)
    b = a[::-1]
    if a == b:
        return True
    else:
        return False


N, K = list(map(int, input().split()))
counter = 0
while True:
    if is_palindromic(N):
        print(N)
        print(counter)
        break
    counter += 1
    if counter > K:
        print(N)
        print(K)
        break
    reversed_n = int(str(N)[::-1])
    N += reversed_n
