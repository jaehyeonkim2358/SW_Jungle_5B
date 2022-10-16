import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
m = [[0]*(N+1) for _ in range(N+1)]

p = []
a,b = map(int,input().split())
p.append(a)
p.append(b)
for i in range(1, N):
    a,b = map(int,input().split())
    p.append(b)

for i in range(1,N+1):
    m[i][i] = 0 # 초깃값 셋팅 (i=j인 경우들)

for i in range(1, N+1) :
    for j in range(i-1, 0,-1) :
        min_value = INF
        for k in range(j,i) :
            temp_value = m[j][k]+m[k+1][i]+p[j-1]*p[k]*p[i]
            if min_value > temp_value :
                min_value = temp_value
        m[j][i]= min_value

print(m[1][N])