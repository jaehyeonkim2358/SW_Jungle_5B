from collections import defaultdict
from heapq import *
import sys
sys.stdin = open("W03/1197/input.txt","r")

# Prim
n, m = map(int, input().split())
adj = defaultdict(lambda: defaultdict(int))
distance = []   # (weight, vertex)
Y = set()
#  adj = { 
#        a : {b:2, c:1, d:3, e:9, f:4},   # a 의 dict안에 없는 v를 호출시 inf값.     
#        b : {c:4, e:3},                    
#        c : {d:8},                         
#        d : {e:7},                         
#        e : {f:5},                         
#        f : {c:2, g:2, h:2},               
#        g : {f:1, h:6},                    
#        h : {f:9, g:8}                     
#        } 
# adj 출력해서 보기
# for key, ddict in adj.items():
#     print(key, ddict.items(), sep=' : ')

for _  in range(m):
    from_, to_, weight = map(int, sys.stdin.readline().split())
    adj[from_][to_] = int(weight)
    adj[to_][from_] = int(weight)

# 초기화
# 정점 아무거나 root로 잡아서 Y에 넣고 시작. dict라서 무조건 a(문제에선 1) 일거라는 보장은 없다.
root = list(adj.keys())[0]
for w, d in adj[root].items():
    heappush(distance, (d, w))
Y.add(root)
cost = 0

# root를 뺀 n-1번 반복
for _ in range(n-1):
    
    next = None
    while distance:
        if (e := heappop(distance))[1] not in Y:    # 아래에서 이미 Y에 들어간 v를 향한 엣지들은 빼주긴 하지만
                                                    # 두 정점 사이 엣지가 여러개일 경우가 있을 수 있기에
                                                    # Y를 향하지 않는 엣지가 나올 때 까지 pop 한다. 그 와중에 최소임은 보장된다.
            Y.add(e[1])  #  vertex
            cost += e[0] #  weight
            next = e
            break
    
    # 힙 안에 원소가 다 사용될 때 까지 Y에 새로운 원소가 추가되지 않으면,
    # 신장트리가 만들어질 가능성이 없는(연결이 끊어진) 그래프이다.
    if not next:
        print(None); break
        

    # distance에 next의 연결정보 추가해줌.
    for w, d in adj[next[1]].items():
        if w not in Y:  # next의 연결관계 중에, 이미 Y에 들어간 v를 향한 것들 빼고 힙에 추가해 준다.
            heappush(distance, (d, w))
    
print(cost)

