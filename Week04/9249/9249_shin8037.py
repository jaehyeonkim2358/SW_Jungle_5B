# import sys

# input=sys.stdin.readline


# def solve():
#     A=[None]+list(input().strip())
#     B=[None]+list(input().strip())

#     table=[[None for _ in range(len(B)+1)] for _ in range(len(A)+1)] # A와 B를 이용해서 2차원 테이블을 만든다

#     answer=0 # 최대 길이를 저장하기위한 변수
#     answer_list=[]
#     for i in range(1,len(A)):
#         for j in range(1,len(B)):
#             if A[i]==B[j]: # 둘이 같으면 이전에 같은 길이에 +1
#                 table[i][j]=table[i-1][j-1]+1
#                 if answer<table[i][j]:
#                     answer=max(answer,table[i][j])
#                     answer_list=[i,j]
#             else:
#                 continue
                

#     print(answer)
#     for i in range(answer_list[0]-answer+1,answer_list[0]+1):
#         print(A[i],end="")

# solve()

##  KMP로 풀 수 없음 접두사의 시작값이 고정되어버리기 때문에 안됨
# import sys

# input=sys.stdin.readline

# string_A=input().strip()+"%"+input().strip()

# def KMP(string_A): # 실패함수 구현
#     N=len(string_A)
#     table=[0]*N # string_A 길이 만큼 초기화
#     j=0
#     for i in range(1, N): # 모든 문자열을 검사하면서
#         while (j>0 and string_A[i] != string_A[j]): # i번째와 j가 일치하지 않는다면 j에서 1을 뺀 값으로 이동시켜버림
#             j=table[j-1]
#         if string_A[i]==string_A[j]: # 둘이 일치하면 i번째 idx에 j에 1을 더한 값을 넣음
#             j=i+1
#             table[i]=j
#     return table



# print(KMP(string_A))


import sys

input=sys.stdin.readline

A=input().strip()
B=input().strip()

string_sum=A+"%"+B

N=len(string_sum) # 합쳐진 string의 길이를 저장

S_A=[i for i in range(N)]
Old_rank=[0]*(N+1)
New_rank=[0]*(N+1)

for i in range(N):
    Old_rank[i]=ord(string_sum[i]) # string_sum ASCII로 변환 -- 알파벳 대소 비교를 보다 쉽게하기 위해서


Old_rank[N]=-1 # 문자열이 끝나는 부분에 -1을 넣어줌
New_rank[N]=-1 # 문자열이 끝나는 부분에 -1을 넣어줌

## Suffix Array를 만드는 부분
t=1 # 동일한 글자일 경우 그 뒤의 글자까지 포함해서 같이 확인하기 위한 변수
while t<N:
    S_A.sort(key=lambda x:(Old_rank[x],Old_rank[min(x+t,N)])) # S_A의 배열은 Old_Rank의 순서를 정렬한 것이되고 그중 동일 등수는 뒤에 숫자를 하나씩 더해가며 작은 순으로 배열을 마침

    for i in range(1,N): 
        p, q=S_A[i-1], S_A[i] #  i-1 번째와 i번째를 사용하기 때문에 i는 1부터 사용 //0부터 쓰면 indexerror

        if Old_rank[p]!=Old_rank[q] or Old_rank[min(p+t,N)] !=Old_rank[min(q+t,N)]:
            New_rank[q]=New_rank[p]+1 #  S_A의 value에 맞는 등수 ex) idx는 등수이고 value는 원래 위치 이걸 S_A에 52번 idx에 0등을 넣어준다
        else:
            New_rank[q]=New_rank[p]

    t=t*2 # t를 2의 지수승으로 늘려나간다 - 시간 복잡도를 줄이는 역할    
    Old_rank=New_rank[:] # 방금 업데이트된 New_rank를 old에 다시 넣고 이 과정이 t가 전체 문자열의 길이를 넘을때까지 반복한다

# 위과정을 끝아로 suffix Array를 만들게됨 New Rank와 Old_rank는 같은 값을 가짐

# LCP array를 만드는 부분
LCP=[0]*N
length=0
for i in range(N):
    k=Old_rank[i] # 새롭게 만들어진 Suffix_array의 첫번째부터 LCP 확인을 시작함
    if k==0: #랭크 리스트를 만들때 길이를 맞춰주기 위해 사용되었던 제일 처음 0번은 무시한다는 의미
        continue

    p=S_A[k-1] # 특수문자로 구분해놓은 구간에서 거꾸로 탐색을 시작함
    # 아래 내용 i+length가 문자열 길이보다 작고 and p+length도 문자열 길이보다 작고 and
    #  전체 문자열의[i+length]의 value와 전체문자열[p+length] 의 value가 같으면 즉 특수문자를 기점으로 제일 앞글자와 특수문자 바로 뒷글자(두번째 input 받은 문자열의 첫글자)가 같으면
    while i+length<N and p+length<N and string_sum[i+length] == string_sum[p+length]:
        length+=1 # 길이를 더해줌 길이를 늘려가면서 확인할꺼야
    LCP[k]=length # 그리고 LCP k번째부터 최대 연속되는 길이를 저장해줌

    if length: # while이 계속 돌면서 나오는 최대길이가 나오고
        length-=1 # 연속이 끊겼기 때문에 1씩 감소를 시킴


m=(0,0) # 이제 전체 길이와 시작 좌표를 출력할꺼
for i, j in enumerate(LCP): # LCP의 index는 시작 좌표가 될꺼고 value는 최장 길이가 될거임
    if 0<=S_A[i-1]+j-1<len(A) and len(A)< S_A[i]+j-1<N: # 좌표+value (만약 해당 좌표부터 끝까지 포함되면 거리상 N이 될수도 있으므로 -1)
        m=max(m,(j,i))
    if 0<=S_A[i]+j-1<len(A) and len(A)< S_A[i-1]+j-1<N:
        m=max(m,(j,i))

print(m[0]) # index 0에는 최장거리 value가 
print(string_sum[S_A[m[1]]:S_A[m[1]]+m[0]]) # index 1에는 좌표가적히게됨