from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]

n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
visit = [[False]*m for _ in range(n)]
Q=deque()
cnt=1
max_width=0
for i in range(n):
    for j in range(m):
        if board[i][j]==1 and visit[i][j]==False:
            visit[i][j]=True
            Q.append((i,j))
            cnt+=1
            width=1
            while Q:
                tmp = Q.popleft()
                for i in range(4):
                   yy = tmp[0]+dy[i]
                   xx = tmp[1]+dx[i]
                   if 0<=yy<n and 0<=xx<m and board[yy][xx]==1 and visit[yy][xx]==False:
                        visit[yy][xx]=True
                        Q.append((yy,xx))
                        width+=1
            if max_width<=width:
                max_width = width


if cnt!=0:
    print(0)
    print(max_width)
else:
    print(cnt)
    print(0)