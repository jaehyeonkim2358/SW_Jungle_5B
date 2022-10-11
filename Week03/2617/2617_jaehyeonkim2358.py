import sys
from collections import defaultdict


def dfs(cur, visited, graph, reverse):
    global v_cnt, r_cnt
    visited[cur] = True
    for g in graph[cur]:
        if not visited[g]:
            if reverse:
                r_cnt += 1
            else:
                v_cnt += 1
            dfs(g, visited, graph, reverse)


def init_visited(n):
    return [False] * (n+1)


n, m = map(int, sys.stdin.readline().split())
check = [False] * (n+1)
v_graph = defaultdict(set)      # 인접리스트, 구슬을 key로 하여 그 구슬보다 가벼운 구슬을 value에 set으로 담는다.
r_graph = defaultdict(set)      # 인접리스트, 구슬을 key로 하여 그 구슬보다 무거운 구슬을 value에 set으로 담는다.
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    v_graph[a].add(b)
    r_graph[b].add(a)



mid = n//2          # 전체 구슬의 절반 갯수

# 어떤 구슬 i보다 
# 무거운 구슬의 갯수가 mid보다 많거나,
# 가벼운 구슬의 갯수가 mid보다 많다면,
# 구슬 i의 무게가 전체의 중간이 될 가능성이 없다.

answer = 0          # 무게가 전체의 중간이 될 가능성이 없는 구슬의 갯수

# 모든 구슬을 순회하며
# 현재 순회중인 구슬보다 가벼운 구슬의 갯수(v_cnt)와
# 현재 순회중인 구슬보다 무거운 구슬의 갯수(r_cnt)를 구한 뒤
# 둘 중 하나라도 전체 구슬의 절반 갯수보다 많다면,
# 그 구슬의 무게는 전체의 중간 무게가 될 가능성이 없는 구슬이다.
for i in range(1, n+1):
    v_visited = init_visited(n)
    r_visited = init_visited(n)
    v_cnt = 0
    r_cnt = 0
    dfs(i, v_visited, v_graph, reverse=False)
    dfs(i, r_visited, r_graph, reverse=True)
    if v_cnt > mid or r_cnt > mid:
        answer += 1

print(answer)
