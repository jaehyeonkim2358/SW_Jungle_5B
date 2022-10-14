import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


class Node():

    def __init__(self, item, left, right):
        # item은 본인 (root node가 됨), left, right는 각각 child node가 됨.
        self.item = item
        self.left = left
        self.right = right
# Node 생성 Node는 자기 자신의 값인 item과 child node의 위치인 left와 right를 가짐.


def preorder(node):
    print(node.item, end='')
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])
    # 전위 순회 root > left child > right child 순으로 순회함.


def inorder(node):
    if node.left != '.':
        inorder(tree[node.left])
    print(node.item, end='')
    if node.right != '.':
        inorder(tree[node.right])
    # 중위 순회 left > root > right 순으로 순회함.


def postorder(node):
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.item, end='')
    # 후위 순회는 left > right > root 순으로 순회함.


N = int(input())
tree = {}
# 노드를 엮어줄 트리 생성 딕셔너리로 받는 이유
# TypeError: list indices must be integers or slices, not str 때문.

for i in range(N):
    node, left, right = map(str, input().split())
    tree[node] = Node(node, left, right)
# 트리에 입력받은 노드 값 입력
# tree[A] = left, right, root node

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])
