"""
start_time: 2019-02-21 19-25-23 周四
坑: 最后一个测试点超时, 改用c++
"""


class Node:
    def __init__(self, addr, next_addr):
        self.addr = addr
        self.next_addr = next_addr


start1, start2, n = input().split()
n = int(n)
hash_map = dict()
for i in range(n):
    addr, _, next_addr = input().split()
    node = Node(addr, next_addr)
    hash_map[addr] = node

# route 用set可能会更快
route = []
cur_addr = start1
while cur_addr != "-1":
    route.append(cur_addr)
    cur_addr = hash_map[cur_addr].next_addr

cur_addr = start2
while cur_addr != "-1":
    if cur_addr in route:
        print(cur_addr)
        exit(0)
    cur_addr = hash_map[cur_addr].next_addr
print(-1)

