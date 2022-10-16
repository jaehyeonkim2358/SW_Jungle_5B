# 평범한 배낭
import sys
input = sys.stdin.readline
print = sys.stdout.write

N, K = map(int, input().split(' '))
items = [[0, 0]] # 1부터 시작하기 위해 그냥 하나 넣어놓은 것
d = [[0]*(K+1) for _ in range(N+1)]

for i in range(N):
    items.append(list(map(int, input().split(' '))))

# sort할 필요 없음
for i in range(1, N+1):
    # i번까지의 아이템으로 j라는 capacity를 넘어서지 않도록 할 수 있는가
    for j in range(1, K+1):
        w, v = items[i]

        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)
    
print(f'{d[N][K]}')
