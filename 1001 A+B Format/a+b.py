a = input()
a, b = a.split()
a = int(a)
b = int(b)
c = a + b
ns = ""
s = str(c)
flag = False
if s[0] == '-':
    flag = True
s = s.strip('-')
idx = len(s)
while idx > 0:
    idx -= 1
    ns += s[idx]
    if idx != 0 and (len(s) - idx) % 3 == 0:
        ns += ','
if flag:
    ns += '-'
print(ns[::-1])




