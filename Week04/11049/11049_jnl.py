# 행렬 곱셈 순서
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
d = []
M = [[0]*(N)for _ in range(N)]
for i in range(N):
    r, c = map(int,input().split(' '))
    d.append(r)
    if i == N-1:
        d.append(c)

for size in range(1, N):
    for start in range(N-size): 
        end = start + size
        
        tmp = sys.maxsize
        for cut in range(start, end):
            tmp = min(tmp, M[start][cut] + M[cut+1][end] + (d[start-1]*d[cut]*d[end]))
        
        M[start][end] = tmp

print(f'{M[0][-1]}')