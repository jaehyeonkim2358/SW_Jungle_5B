import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

V = int(input())
E = int(input())
graph = {i: [] for i in range(1, V + 1)}

for _ in range(E):
    sv, ev = map(int, input().split())
    graph[sv].append(ev)
    graph[ev].append(sv)


def dfs(sv):
    if sv in visited:
        return
    visited.add(sv)
    for i in graph[sv]:
        dfs(i)
    return len(visited)-1


visited = set()
print(dfs(1))
