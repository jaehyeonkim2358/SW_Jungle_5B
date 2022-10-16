import sys
input=sys.stdin.readline

N,M=map(int,input().strip().split())

A=set()
for i in range(M): # 밟아서는 안되는 돌의 정보를 저장, 중복이 없다는 말이 문제에 없기 때문에 set 을 추천
    A.add(int(input().strip()))

answer=0
dp=[[N+1]*(int((2*N)**0.5)+2) for _ in range(N+1)] # y축은 돌의 number x축은 속도
# int((2*N)**0.5)+2 // +2 하는 이유
# 1. 루트를 쓰게 되면 소수점이 나오는데 이를 정수형으로 바꾸면 내림이 됨 --> 이를 방지하기 위해서 +1
# 2. 돌의 Number를 index와 맞춰주기 위해서 1을 더 함
# 따라서 총 +2를 하게 됨

def jump():
    global answer
    dp[1][0]=0 # 시작하는 돌 1은 점프 거리가 0임
    for i in range(2, N+1): # 2번 돌부터 N번돌까지 가야하니깐
        if i in A : # 내가 가야할 돌이 가선 안될 돌의 위치에 있음
            continue # 무시하고 가자
        for v in range(1,int((2*N)**0.5)+1): # 1번에서 부터 한계까지
            dp[i][v]=min(dp[i-v][v-1],dp[i-v][v],dp[i-v][v+1])+1 # 이전 속도에서 -1, 0, +1 한 경우의 수중에 최소 값(가장 회수가 적어야하니깐)을 가져오고 거기에 +1(가속)
    
    answer=min(dp[N])

jump()

if answer==N+1:
    print(-1)
else:
    print(answer)

# ref : https://velog.io/@grace0st/%EC%A0%90%ED%94%84-%EB%B0%B1%EC%A4%80-2253%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC