import sys

N, K = map(int, sys.stdin.readline().split())
money = []
for _ in range(N):
    tmp = int(sys.stdin.readline().rstrip())
    if tmp <= K:
        money.append(tmp)


count = 0
for i in range(len(money)-1, -1, -1):
    count += K//money[i]
    K -= (K//money[i])*money[i]

sys.stdout.write(f'{count}')