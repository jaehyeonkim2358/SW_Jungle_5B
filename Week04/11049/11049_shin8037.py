import sys

input=sys.stdin.readline

N=int(input())

A=[]
for i in range(N):
    A.append(list(map(int,input().strip().split())))

dp=[[0]*N for _ in range(N)]

for i in range(1,N): # i==i는 0이기 때문에 1부터 진행
    for j in range(N-i): # j는 행 j,j는 0이라서 빼고
        x=j+i # 여기는 열 j+i 만큼가야함
        dp[j][x]=sys.maxsize
        for k in range(j,x): # k는 행렬 중간 괄호의 위치
            dp[j][x]=min(dp[j][x],dp[j][k]+dp[k+1][x]+A[j][0]*A[k][1]*A[x][1]) # 점화식 계산법

print(dp[0][N-1])