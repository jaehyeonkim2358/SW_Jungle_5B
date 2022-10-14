import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
# 328536KB / 1196ms


def dfs(node):
    global cnt
    visited[node] = True
    for next_node in graph[node]:
        if place[next_node] == 1:
            cnt += 1
            # next node가 실내일 경우 (실외 - 실내)
        elif visited[next_node] == False and place[next_node] == 0:
            dfs(next_node)
            # 방문하지 않았고 실외인 경우 (실외 - 실외)


N = int(input())
in_out = list(map(int, input().rstrip()))
place = {i: 0 for i in range(1, N+1)}
visited = {i: False for i in range(1, N+1)}
ans = 0
for i in range(1, N + 1):
    place[i] = in_out[i-1]

graph = defaultdict(list)
for _ in range(N-1):
    sv, ev = map(int, input().split())
    graph[sv].append(ev)
    graph[ev].append(sv)

    if place[sv] == 1 and place[ev] == 1:
        ans += 2


for i in range(1, N+1):
    cnt = 0
    if visited[i] == False and place[i] == 0:
        dfs(i)
        ans += cnt*(cnt-1)

print(ans)
