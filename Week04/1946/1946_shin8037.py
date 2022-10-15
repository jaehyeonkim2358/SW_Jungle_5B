# 1차시도 두개를 다 리스트로 받아서 정렬하기
# 57760kb 5168ms

# import sys
# input=sys.stdin.readline


# N=int(input().strip())

# def solve():
#     for _ in range(N):
#         k=int(input().strip())
#         A=[]
#         cnt=1 # 자기 자신 포함
#         for _ in range(k):
#             A.append(list(map(int,input().strip().split())))
        
#         A.sort(key=lambda x:(x[0],x[1])) # 오름차순으로 정렬
#         s=A[0][0] # 서류
#         e=A[0][1] # 면접
#         for i in range(1,len(A)):            
#             if A[i][0]<s or A[i][1]<e: # 둘중 하나라도 범위 안에 있으면 카운트 추가
#                 cnt+=1 
#                 s=A[i][0] # 범위에 들어간 애가 새로운 기준이 되어줌
#                 e=A[i][1]
        
#         print(cnt)

# solve()

# 2차시도 
# 35476kb 2008ms
import sys
input=sys.stdin.readline

def solve():
    N=int(input().strip())
    for _ in range(N):
        k=int(input().strip())
        A=[0]*(k+1) # 인덱스 = 서류, 값이 면접으로 만들기위한 리스트
        cnt=1
        for _ in range(k):
            a,b=(map(int,input().strip().split()))
            A[a]=b # 인덱스 - 서류, 값 - 면접
        
        e=A[1] # 인덱스 별로 서류를 정렬하였기때문에 뒤에 면접 값만 비교하면됨
        for i in range(1,len(A)):
            if A[i]<e: # 면접 값이 더 작으면
                cnt+=1 # 카운트 세주고
                e=A[i] # 걔가 새로운 기준
        
        print(cnt)

solve()