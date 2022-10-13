import sys

input=sys.stdin.readline

N=int(input())

start=2
dp=[0]*91
dp[1]=1

def solve(i):
    if N<=1:
        print(dp[N])
    elif dp[N]!=0:
        print(dp[N])
    else:
        dp[i]=dp[i-2]+dp[i-1]        
        solve(i+1)
    

solve(start)