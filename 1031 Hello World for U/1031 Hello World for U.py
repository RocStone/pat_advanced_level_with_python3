"""
start_time: 2019-02-21 19-13-41 周四
end_time: 2019-02-21 19-24-58 周四
"""

raw = input()
n = len(raw)
a, b = 0, 0
aa, bb = 0, 3
while bb <= n:
    if (n - bb) % 2 == 0:
        aa = (n + 2 - bb) / 2
        if bb >= aa > a:
            a = aa
            b = bb
    bb += 1

a, b = int(a), int(b)
spaces = b - 2
for i in range(a - 1):
    print(f"{raw[i]}{' ' * spaces}{raw[-i - 1]}")
print("".join(raw[a - 1:a - 1 + b]))
