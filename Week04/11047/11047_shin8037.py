import sys

input=sys.stdin.readline

N,K=map(int,input().strip().split())

coins=[]
for i in range(N):
    coins.append(int(input()))


result=0
for i in range(N-1,-1,-1):
    result+=K//coins[i]
    K =K-(K//coins[i])*coins[i]
    if K==0:
        break

print(result)
