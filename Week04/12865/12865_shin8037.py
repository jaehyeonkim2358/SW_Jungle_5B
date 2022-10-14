import sys

input=sys.stdin.readline

N,k=map(int,input().strip().split())

A=[[0,0]] # input의 순서와 N,k를 이용한 dp table의 순서를 맞춰주기 위해서
for i in range(N):
    A.append(list(map(int,input().strip().split())))

A.sort() # 해도 되고 안해도 되고

dp=[[0]*(k+1) for _ in range(N+1)] # dp를 만들어줌 2차원으로 앞의 LCS 문제랑 비슷한 유형

for i in range(1,N+1):
    for j in range(1, k+1):
        weight, val=A[i][0],A[i][1] # 각각의 weight와 val을 저장
        if j<weight: # j가 현재 weight보다 작으면 이전 값을 복사
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight]+val) # 이전 value와 현재 value 중 max를 저장 dp[i-1][j-weight]+val --> 앞선 dp[i-1][j] 에서 배낭에 넣을 weight를 빼고 그부분에 해당하는 val이 있으면 그걸 합쳐준다는 의미
        
            
print(dp[N][k])