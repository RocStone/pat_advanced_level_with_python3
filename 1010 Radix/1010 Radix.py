def binary_search(left, right):
    global target
    if left > right:
        print('Impossible')
        exit(0)
    mid = (left + right) // 2
    new_var = [alphabet[ord(each) - ord('0')] * mid ** i for i, each in enumerate(reversed(list(var)))]
    new_var = sum(new_var)
    if new_var == target:
        print(mid)
        exit(0)
    elif new_var > target:
        binary_search(left, mid - 1)
    else:
        binary_search(mid + 1, right)


n1, n2, tag, radix = [str(each) for each in input().split()]
tag, radix = int(tag), int(radix)
alphabet = [i for i in range(0, 10)]
alphabet.extend([0 for i in range(10, 49)])
alphabet.extend([i - 39 for i in range(49, 49 + 26)])

target = n1
var = n2
if tag == 2:
    target = n2
    var = n1
target = reversed(list(target))
target = [alphabet[ord(each) - ord('0')] * radix ** i for i, each in enumerate(target)]
target = sum(target)
# 计算最小进制
start_radix = 0
for each in list(var):
    if start_radix < alphabet[ord(each) - ord('0')]:
        start_radix = alphabet[ord(each) - ord('0')]
start_radix += 1

# 这里有坑，比如11 b 1 10，这种输入直接就已经相等了，那么输出最小的进制就行，用二分出来的结果不是最小的
# 这就是题目中提到的，如果结果不唯一，就输出最小的，以后看到这种提示，一定要写在纸上
new_var = [alphabet[ord(each) - ord('0')] * start_radix ** i for i, each in enumerate(reversed(list(var)))]
new_var = sum(new_var)
if new_var == target:
    print(start_radix)
    exit(0)
# 排除这种情况，正常用二分查找
binary_search(start_radix, 10**100)
