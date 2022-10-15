#######재귀 카운트 세는 부분에 문제가 있음 추후 수정 예정
# import sys

# input=sys.stdin.readline

# N=int(input())

# A=[]
# for i in range(N):
#     A.append(list(map(int,input().strip().split())))

# sorted(A,key=lambda x: (x[1],x[0]))

# print(A)
# answer=0
# def solve(e,i,cnt):
#     global answer
#     for j in range(i+1,N):
#         s2,e2=A[j]
#         if s2>=e:
#             cnt+=1
#             solve(e2,j,cnt)
            
#     answer=max(cnt,answer)
        

# for i in range(N):
#     s,e=A[i]
#     cnt=0
#     solve(e,i,cnt)
# print(answer)


import sys

input=sys.stdin.readline

N=int(input().strip())

A=[]
for i in range(N):
    A.append(list(map(int,input().strip().split())))

A=sorted(A,key=lambda x: (x[1],x[0])) # 끝나는 시간 오름차순 정렬 + 시작시간 오름차순 정렬

cnt=1 # 처음꺼 포함해야해서 1
e=A[0][1] # 처음 시작하는 회의의 끝나는 시간을 저장
for i in range(1,N):
    if A[i][0]>=e: #현재 회의의 끝나는 시간보다 다음 회의의 시작시간이 늦거나 같으면
        cnt+=1 # 카운트 추가해주고
        e=A[i][1] # 끝나는 시간 변경

print(cnt)