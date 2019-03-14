from math import inf


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinaryTree:
    def __init__(self):
        self.root = None
        self.mirror = False

    def add_node(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
        else:
            cur_node = self.root
            while True:
                if node.value < cur_node.value and not self.mirror or node.value >= cur_node.value and self.mirror:
                    if cur_node.left is None:
                        cur_node.left = node
                        break
                    else:
                        cur_node = cur_node.left
                else:
                    if cur_node.right is None:
                        cur_node.right = node
                        break
                    else:
                        cur_node = cur_node.right

    def preorder(self):
        stack = [self.root]
        preorder = []
        while stack:
            cur_node = stack.pop()
            preorder.append(cur_node.value)
            if cur_node.right is not None:
                stack.append(cur_node.right)
            if cur_node.left is not None:
                stack.append(cur_node.left)
        return " ".join(list(map(str, preorder)))

    def postorder(self):
        stack = [self.root]
        postorder = []
        while stack:
            cur_node = stack.pop()
            if type(cur_node) == int:
                postorder.append(cur_node)
            else:
                stack.append(cur_node.value)
                if cur_node.right is not None:
                    stack.append(cur_node.right)
                if cur_node.left is not None:
                    stack.append(cur_node.left)
        return " ".join(list(map(str, postorder)))


n = int(input())
bt = BinaryTree()
input_preorder = input()
for each in list(map(int, input_preorder.split())):
    bt.add_node(each)

if bt.preorder() == input_preorder:
    print('YES')
    print(bt.postorder())
    exit(0)

# 也许是mirror树呢？
bt.mirror = True
bt.root = None
for each in list(map(int, input_preorder.split())):
    bt.add_node(each)
if bt.preorder() == input_preorder:
    print('YES')
    print(bt.postorder())
    exit(0)

# 那就不可能了
print('NO')
