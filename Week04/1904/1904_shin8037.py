import sys

input=sys.stdin.readline

N=int(input())

dp=[0]*(N+1)


def dynamic_(n):
    if n<2:
        dp[0]=1
        dp[1]=1
        return dp[n]
    else: 
        dp[0]=1
        dp[1]=1       
        for i in range(2,n+1):
            dp[i]=(dp[i-1]%15746+dp[i-2]%15746)%15746
        return dp[i]


print(dynamic_(N))