"""
start time: 2019年2月20日22:24:21
end time: 2019年2月20日22:30:22
"""

string1 = input()
string2 = str(int(string1)*2)
sorted_s1 = list(string1)
sorted_s1.sort()
sorted_s2 = list(string2)
sorted_s2.sort()
if sorted_s1 == sorted_s2:
    print('Yes')
else:
    print('No')
print(string2)
