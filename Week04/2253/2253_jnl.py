# 점프
import sys
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(10**8)

# dp[stone][step]의 의미
# stone step의 환경에서 N번째 도시에 딱 맞게 도착할 수 있는 최소 점프 횟수

N, M = map(int, input().split(' '))
dp = [[-1]*(int((2 * N)** 0.5) + 2) for _ in range(N+1)]
small = set()
for _ in range(M):
    small.add(int(input()))

flag = False
def solution(step, stone):
    global flag
    if stone == N:
        flag = True
        return 0

    if dp[stone][step] != -1:
        return dp[stone][step]

    dp[stone][step] = N+2
    for i in range(step-1, step+2):
        if i <= 0:
            continue
        new_stone = stone + i
        if (new_stone <= N) and (new_stone not in small):
            dp[stone][step] = min(dp[stone][step], 1+solution(i, new_stone))
    return dp[stone][step]
answer = solution(0, 1)
if flag:
    print(f'{answer}')
else:
    print('-1')
