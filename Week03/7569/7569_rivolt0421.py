from collections import deque
import sys
sys.stdin = open("W03-W04/Week03/7569/input.txt","r")

m, n, h = map(int, input().split())

q = deque()
tomatos = []
# tomatos[층][행][열]
raw = 0
for i in range(h):
    p = []
    for j in range(n):
        line = list(map(int, sys.stdin.readline().split()))
        for k in range(m):
            if line[k] == 1 :       # 익은 토마토
                q.append((i,j,k))   # 익은 토마토 위치 q에 넣어주기
            elif line[k] == 0:
                raw += 1
        p.append(line)
    tomatos.append(p)

# 벌써 raw가 0 이면 이미 다 익었다.
if not raw:
    print(0); exit(0);

def bound(z,y,x):
    if z < 0 or z >= h:
        return False
    if y < 0 or y >= n:
        return False
    if x < 0 or x >= m:
        return False
    return True
        
steps = -1
while q:
    adj_cnt = len(q)
    steps += 1
    while adj_cnt > 0:
        z,y,x = q.popleft()
        for dz,dy,dx in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
            nz = z+dz; ny = y+dy; nx = x+dx
            if bound(nz,ny,nx) and not tomatos[nz][ny][nx]:
                tomatos[nz][ny][nx] = 1
                raw -= 1
                q.append((nz,ny,nx))
        adj_cnt -= 1

if not raw: # 안 익은 토마토 들이 전부 처리되어 raw가 0이 되었다. 
    print(steps)
else:       # 아직 안 익은 토마토가 남아서 raw가 0이 아니다.
    print(-1)