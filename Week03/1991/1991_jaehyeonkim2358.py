import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
nodes = dict()
for _ in range(n):
    temp = input().split()
    nodes[temp[0]] = [temp[1], temp[2]]


def preorder(root):
    if root == '.':
        return
    print(f'{root}')
    preorder(nodes[root][0])
    preorder(nodes[root][1])


def inorder(root):
    if root == '.':
        return
    inorder(nodes[root][0])
    print(f'{root}')
    inorder(nodes[root][1])


def postorder(root):
    if root == '.':
        return
    postorder(nodes[root][0])
    postorder(nodes[root][1])
    print(f'{root}')



preorder('A')
print('\n')
inorder('A')
print('\n')
postorder('A')