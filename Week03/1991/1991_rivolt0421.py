import sys
sys.stdin = open("W03/1991/input.txt","r")

n = int(input())
d = dict([(p, (l, r)) for p,l,r in[line.split() for line in sys.stdin.read().strip().split("\n")]])

# 문제 조건 : A가 항상 루트노드

def traversal(node, order):
    if node == '.':
        return
    
    l = d[node][0]
    r = d[node][1]
    
    if order == 'pre':
        print(node, end=''); traversal(l,order); traversal(r, order)
    elif order == 'in':
        traversal(l,order); print(node, end=''); traversal(r, order)
    else: # order == 'post'
        traversal(l,order); traversal(r, order); print(node, end='')

traversal('A', 'pre'); print()
traversal('A', 'in'); print()
traversal('A', 'post'); print()