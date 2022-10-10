import sys
sys.stdin = open("W03-W04/Week03/11724/input.txt","r")
sys.setrecursionlimit = 10**6

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find(parent, x):
    if parent[x] != x:
        root_parent = find(parent, parent[x])
        parent[x] = root_parent
        return root_parent
    else:
        return x

def union(u, w, parent):
    u = find(parent, u)
    w = find(parent, w)
    
    if u!=w:
        if u < w: parent[u] = w
        else: parent[w] = u

    
for _ in range(m):
    u, w = map(int, sys.stdin.readline().split())
    union(u, w, parent)
for x in range(n+1):
    find(parent, x)

        
print(len(set(parent))-1)
