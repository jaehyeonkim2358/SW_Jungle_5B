# 11053: 가장 긴 증가하는 부분 수열
# A = {10, 20, 10, 30, 20, 50} 
# 가장 긴 증가하는 부분 수열 10, 20, 30, 50 이고, 길이는 4
# LIS는 완전탐색, DP, 이진탐색으로 구현이 가능하다.

import sys
sys.stdin = open("11053/input.txt","r")
N = int(input())    # 수열 A의 크기 N
A = list(map(int, input().split())) # 수열 A를 이루고 있는 Ai

dp = [1] * N # 수열의 크기를 저장할 dp 테이블을 먼저 만들어줌

for i in range(1, N): # dp[0]은 무조건 1이기 때문에 1부터 시작
    for j in range(i):
        if A[i] > A[j]:
            # 수열의 크기가 저장되어진 리스트 
            dp[i] = max(dp[i], dp[j]+1)
            print(dp)

print(max(dp))
# 수열의 크기를 저장하는 dp 테이블에서 max 값이 가장 긴 증가하는 부분 수열의 길이이다. 

# 핵심: 길이를 찾으려는 숫자가 비교할 숫자보다 크면, 
# 그 숫자가 가지고 있는 길이 +1과 자신의 길이를 비교해서 큰 값으로 최신화한다. 