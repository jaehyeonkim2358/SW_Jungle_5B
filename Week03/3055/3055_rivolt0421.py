from collections import deque
import sys
sys.stdin = open("W03-W04/Week03/3055/input.txt","r")

R, C = map(int, sys.stdin.readline().split())

forest = []; spring = set(); visited = set()
S = ()
for i in range(R):
    line = sys.stdin.readline().strip()
    for j,a in enumerate(line):
        if a == 'S' : S = ('S', i,j); visited.add((i,j))
        if a == '*' : spring.add((i,j))
    forest.append(line)

# forest 구조에 따라 숫자 배열을 따로 만들면 메모리 초과.
# encode = {'.':0, 'S':0 , '*':1 , 'X':1 , 'D':float('inf')}
# for i in range(R):
#     l = []
#     for j,a in enumerate(sys.stdin.readline().strip()):
#         if a == 'S' : S = (i,j)
#         if a == '*' : spring.append((i,j))
#         l.append(encode[a])
#     forest.append(l)
    
def bound(nr,nc):
     if nr < 0 or nr >= R:
         return False
     if nc < 0 or nc >= C:
         return False
     if (nr,nc) in spring:
         return False
     return True

def flood(v, q, spring, forest):
    for d in (1,-1):
        for nr,nc in [(v[1]+d,v[2]), (v[1],v[2]+d)]:
            if bound(nr,nc) and forest[nr][nc] in '.S':
                spring.add((nr,nc))
                q.append(('*',nr,nc))
                
def flee(v, q, forest):
    for d in (1,-1):
        for nr,nc in [(v[1]+d,v[2]), (v[1],v[2]+d)]:
            if bound(nr,nc) and (nr,nc) not in visited:
                if forest[nr][nc] == '.':
                    q.append(('S', nr,nc))
                    visited.add((nr,nc))
                elif forest[nr][nc] == 'D':
                    q.append(('D', nr,nc))      # 여기서 appendleft해줬다가 한참 해맸다.
                                                # appendleft해주면 step이 지켜지지 않음.
     
q = deque()
for s in spring:
    q.append(('*',s[0],s[1]))
q.append(S)

# 물과 고슴도치 BFS 한번에 다 실행. 대신 물이 먼저 움직이게만 하면 됨.
def go(q):
    step = 0
    while q :
        adj_cnt = len(q)
        while adj_cnt > 0:
            v = q.popleft()
            if v[0] == 'D':
                print(step)
                return True
            elif v[0] == '*':
                flood(v, q, spring, forest)
            elif v[0] == 'S':
                flee(v, q, forest)
            adj_cnt -= 1
        step += 1

    return False

if not go(q):
    print('KAKTUS')