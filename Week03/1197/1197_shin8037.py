import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8) # 재귀함수 돌다가 limit에 걸리지 않게 해제


def compare_PN(parent_node,x):  # 부모 노드와 input 값이 같은 것을 찾을때 까지 재귀 (루트 노드 확인과정)
    if parent_node[x]==x:
        return x
    parent_node[x]=compare_PN(parent_node,parent_node[x])

    return parent_node[x]

def union_PN(parent_node,a,b): # a, b의 부모 노드가 다르면 둘 중 작은 값으로 맞춰줌
    a=compare_PN(parent_node,a)
    b=compare_PN(parent_node,b)

    if a<b:
        parent_node[b]=a
    else:
        parent_node[a]=b

def solve() :
    cost =0
    for i in A: # 간선을 기준으로 for문을 돌릴꺼야 최소값을 구해야하니깐
        c,a,b=i
        if compare_PN(parent_node,a) != compare_PN(parent_node,b):
            union_PN(parent_node,a,b)
            cost+=c # 위 두 과정을 모두 통과하면 최소 비용 + 사이클이 생기지 않았다는 의미 --> 비용 추가
    return cost


N,k=map(int,input().strip().split())

A=[] # 간선 리스트
for i in range(k):
    a,b,c=map(int,input().strip().split())
    A.append([c,a,b])

A.sort() # 간선 리스트를 비용순서로 재배열 - 크루스칼 알고리즘을 쓰기 위한 준비

parent_node=[] # 부모 노드 리스트
for i in range(N+1):
    parent_node.append(i)

print(solve())
