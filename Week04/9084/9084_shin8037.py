import sys

input=sys.stdin.readline

N=int(input().strip())

for i in range(N):
    M=int(input().strip())
    coins=list(map(int,input().strip().split()))
    purpose=int(input().strip()) # 목표금액
    dp=[0]*(purpose+1) # 목표금액에 맞는 dp 공간 확보
    dp[0]=1 # 0번에 1을 넣어야 1을 1원으로 맞출수 있음
    for coin in coins:
        for j in range(1, purpose+1):
            if j >= coin:
                dp[j]+=dp[j-coin] # 동전 개수 점화식 ex) j=10 coin = 5이면  dp[10]= dp[10]+dp[5] : 기존 dp[10]에 있던 개수 + dp[5]원을 넣었을때 생기는 동전 합 개수표시
    print(dp[purpose])
        
