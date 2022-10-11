import sys
sys.stdin = open("W03/1197/input.txt","r")
# E = [(u,w,d) for u,w,d in [map(int,line.split()) for line in sys.stdin.read().strip().split('\n')]]
# 한 줄로 입력받는거 메모리 낭비, 시간 낭비 심하다. 쓰지 말자.

# Kruskal
# 초기화
n, m = map(int, input().split())

E = []
for _ in range(m):
    E.append(list(map(int, sys.stdin.readline().split())))
E.sort(key=lambda x: x[2])

parent = [x for x in range(n+1)]
# 초기화 끝

def find(parent, x):
    if parent[x] != x:
        root_parent = find(parent, parent[x]) # 재귀 호출
        parent[x] = root_parent # 경로 압축.
                                # root_parent 바로 반환하지 않고
                                # 콜 스택의 함수마다 parent[x] 값을 가장 최상위 부모로 갱신해줌.
        return root_parent
    
    return x

cost = 0
cnt = 0
for u,w,d in E:
    
    # 부모가 같다면 사이클이므로 지나감.
    if (u_p := find(parent, u)) == (w_p := find(parent, w)):
        continue
    
    # 루트를 합치는 기준이 있는 것이 더 빠르다.
    # 루트를 갱신할 때는, 루트의 루트를 갱신하는 것이다. 자식들의 루트를 갱신(parent[w]=u_p)하면 오류다.
    if u_p < w_p:
        parent[w_p] = u_p
    else:
        parent[u_p] = w_p
        
    cost += d
    cnt += 1
    if  cnt >= n-1: # 간선이 n-1개 만들어 졌다면 더이상 다른 엣지를 확인할 필요 없음.
        break
    
if cnt != (n-1):
    print("fail to make MST")
else:
    print(cost)