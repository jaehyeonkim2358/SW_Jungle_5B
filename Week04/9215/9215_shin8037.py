import sys

input=sys.stdin.readline

A=[0]+list(input().strip())

B=[0]+list(input().strip())

table=[[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)] # A와 B를 이용해서 2차원 테이블을 만든다

answer=0 # 최대 길이를 저장하기위한 변수
for i in range(1,len(A)):
    for j in range(1,len(B)):
        if A[i]==B[j]: # 둘이 같으면 이전에 같은 길이에 +1
            table[i][j]=table[i-1][j-1]+1
            answer=max(answer,table[i][j])
        elif table[i-1][j]>=table[i][j-1]: # 다르다면 이전 큰 값을 그대로 복사
            table[i][j]=table[i-1][j]
        elif table[i][j-1]>=table[i-1][j]:
            table[i][j]=table[i][j-1]
        else:
            table[i][j]=0

print(answer)