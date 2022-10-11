# dictionary 사용

import sys,copy
from collections import defaultdict, deque
sys.setrecursionlimit(10**8)

input=sys.stdin.readline

N,M=map(int,input().strip().split())

compare_list=defaultdict(list) # 간선의 연결 정보를 dictionary로 받음
for i in range(M):
    a,b=map(int,input().strip().split())
    compare_list[a].append(b)

A=[0]*(N+1) # 각 노드가 받은 간선의 횟수를 넣음
for i in range(1,N+1): 
    for j in range(len(compare_list[i])):
        x=compare_list[i][j]
        A[x]+=+1
A2=copy.deepcopy(A) # 간선 정보를 복사해놓음

result=[]
def topologySort():
    dq=deque()
    for key in compare_list.keys():
        if A[key]==0: # 초기 간선을 받은 횟수가 0이라면 진입로라는 뜻
            dq.append(key)
            while dq:
                x=dq.popleft()
                result.append(x)
                for k in compare_list[x]:
                    A2[k]-=1
                    if A2[k]==0:
                        dq.append(k)

topologySort()
print(*result)
