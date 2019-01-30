k1, *seq1 = [float(each) for each in input().split()]
k2, *seq2 = [float(each) for each in input().split()]
k1 = int(k1)
k2 = int(k2)
p = [0] * 2001
for i in range(k1):
    for j in range(k2):
        index = int(seq1[i * 2] + seq2[j * 2])
        p[index] += seq1[i * 2 + 1] * seq2[j * 2 + 1]
counter = 0
result = []
for i in range(2000, -1, -1):
    if p[i] != 0:
        counter += 1
        result.append(str(i))
        result.append(str(round(p[i], 1)))
print('{} '.format(counter) + ' '.join(result))
