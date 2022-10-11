import sys
sys.stdin = open('1991/1991_lwh.txt', 'r')
input = sys.stdin.readline

def preorder(tree, root):
    result = []
    def visit(node, left_child, right_child):
        result.append(node)
        if tree[node][0] != '.':
            visit(left_child, tree[left_child][0], tree[left_child][1])
        if tree[node][1] != '.':
            visit(right_child, tree[right_child][0], tree[right_child][1])
    
    visit(root, tree[root][0], tree[root][1])
    print(''.join(result))

def inorder(tree, root):
    result = []
    def visit(node, left_child, right_child):
        if tree[node][0] != '.':
            visit(left_child, tree[left_child][0], tree[left_child][1])
        result.append(node)
        if tree[node][1] != '.':
            visit(right_child, tree[right_child][0], tree[right_child][1])

    visit(root, tree[root][0], tree[root][1])
    print(''.join(result))

def postorder(tree, root):
    result = []
    def visit(node, left_child, right_child):
        if tree[node][0] != '.':
            visit(left_child, tree[left_child][0], tree[left_child][1])
        if tree[node][1] != '.':
            visit(right_child, tree[right_child][0], tree[right_child][1])
        result.append(node)

    visit(root, tree[root][0], tree[root][1])
    print(''.join(result))

tree = dict()
N = int(input())
root = ''
for _ in range(N):
    node = input().rstrip().replace(' ','')
    tree[node[0]] = node[1:]
    if not root:
        root += node[0]

preorder(tree, root)
inorder(tree, root)
postorder(tree, root)