line1 = input()
line2 = input()
line1 = line1.split()
line2 = line2.split()
k1 = int(line1[0])
k2 = int(line2[0])
p1 = [0.0] * 1001
p2 = [0.0] * 1001

for i in range(k1):
    idx = int(line1[i * 2 + 1])
    p1[idx] = float(line1[i * 2 + 2])

for i in range(k2):
    idx = int(line2[i * 2 + 1])
    p2[idx] = float(line2[i * 2 + 2])

p3 = [p1[i] + p2[i] for i in range(1001)]
k3 = 0
for p in p3:
    if p != 0:
        k3 += 1
print(k3, end='')
for i in range(1000, -1, -1):
    if p3[i] != 0:
        print(' {} {}'.format(i, round(p3[i], 1)), end='')


