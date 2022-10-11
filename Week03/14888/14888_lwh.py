import sys
sys.stdin = open('14888/14888_lwh.txt', 'r')
input = sys.stdin.readline

def dfs(idx, ans):
    global plus, minus, times, divide, min_ans, max_ans, N

    if idx == N:
        max_ans = max(max_ans, ans)
        min_ans = min(min_ans, ans)

    else:
        if plus > 0:
            plus -= 1
            dfs(idx + 1, ans + A_list[idx])
            plus += 1
        if minus > 0:
            minus -= 1
            dfs(idx + 1, ans - A_list[idx])
            minus += 1
        if times > 0:
            times -= 1
            dfs(idx + 1, ans * A_list[idx])
            times += 1
        if divide > 0:
            divide -= 1
            dfs(idx + 1, int(ans / A_list[idx]))
            divide += 1

N = int(input())
A_list = list(map(int, input().split()))
plus, minus, times, divide = map(int, input().split())
max_ans = -1e9
min_ans = 1e9
dfs(1, A_list[0])
print(max_ans)
print(min_ans)

