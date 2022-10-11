import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('5639/5639_lwh.txt', 'r')
input = sys.stdin.readline

def bi_search(start, end, target):
    res = end
    while True:
        mid = (start + end)//2
        if nodes[mid] < target:
            start = mid + 1
            res = mid
        else:
            end = mid - 1 
        if start > end:
            break
    return res

def postorder(root, end):
    if root > end:
        return
    if root == end:
        print(nodes[root])
        return
    border = bi_search(root + 1, end, nodes[root])
    postorder(root + 1, border)
    postorder(border + 1, end)
    print(nodes[root])

nodes = []
while True:
    num = input().rstrip()
    if not num:
        break
    nodes.append(int(num))

postorder(0, len(nodes) - 1)


