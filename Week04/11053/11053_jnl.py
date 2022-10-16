# 가장 긴 증가하는 부분 수열
import sys 
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
A = list(map(int, input().split(' ')))
dp = [1 for _ in range(N)]
for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            # dp[j]+1 의 의미: j번째 값에 대한 증가하는 부분 수열의 최대 길이에다가 하나 더 붙여주는 꼴이니까
            dp[i] = max(dp[i], dp[j]+1)
            

print(f'{max(dp)}')