import sys
sys.stdin = open('Week04/11049/11049_lwh.txt', 'r')
input = sys.stdin.readline

INF = 2**31

N = int(input())
p = list(map(int, input().split()))
for _ in range(N-1):
    p.append(list(map(int, input().split()))[1])

m = [[INF] * (N +1) for _ in range(N+1)]

for i in range(1, N+1):
    m[i][i] = 0

for l in range(2, N + 1):
    for i in range(N - l + 2):
        j = i + l - 1
        C = p[i-1]*p[j]
        for k in range(i, j):
            m[i][j] = min(m[i][k] + m[k + 1][j] + C*p[k], m[i][j])

print(m[1][N])