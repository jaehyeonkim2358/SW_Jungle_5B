import sys

input=sys.stdin.readline

N=int(input())

A=(list(map(int,input().strip().split())))

dp=[0]*N



for i in range(N):
    for j in range(i):
        if A[i]>A[j] and dp[i]<dp[j]: # A[i]가 A[j] 보다 크고 --> A 리스크 안에 값이 더 크고 dp[i] 가 dp[j] 보다 작다는 이전에 등록된 길이랑 비교를 한다
            dp[i]=dp[j] # dp[i]< dp[j]보다 작으면 더 큰 길이를 현재 값에 넣어주고
    dp[i]+=1 # 그 길이에 현재 value에 해당하는 길이 1을 추가해준다

print(max(dp))