# class python 시간초과 pypy 메모리초과

import sys
sys.stdin = open('5639/5639_lwh.txt', 'r')

input = sys.stdin.readline

class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def add(self, key):
        def add_node(node, key):
            if key < node.key:
                if node.left is None:
                    node.left = Node(key, None, None)
                else:
                    add_node(node.left, key)
            else:
                if node.right is None:
                    node.right = Node(key, None, None)
                else:
                    add_node(node.right, key)
            return True
        
        if self.root is None:
            self.root = Node(key, None, None)
            return True
        else:
            return add_node(self.root, key)

    def dump(self):
        def print_subtree(node):
            if node is not None:
                print_subtree(node.left)
                print_subtree(node.right)
                print(node.key)

        print_subtree(self.root)

bst = BinarySearchTree()
while True:
    node = input().rstrip()
    if not node:
        break
    bst.add(int(node))
bst.dump()

# 들어오는 순서 -> 전위 순회 인걸 최대한 이용해야할듯



