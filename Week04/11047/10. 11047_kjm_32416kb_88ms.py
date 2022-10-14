# https://www.acmicpc.net/problem/11047

import sys
from collections import deque
deq = deque()
input = sys.stdin.readline
N,K = map(int, input().split())

for i in range(N):
    deq.appendleft(int(input()))
# print(deq)

count=0
for coin in deq:
    if K >0:
        if coin > K:
            continue
        else:
            tmp_value= (K//coin)
            K = K - coin*tmp_value
            count= count + tmp_value
print(count)


# 재현이 코드 리뷰
# import sys
# N, K = map(int, sys.stdin.readline().split())
# money = []
# for _ in range(N):
#     tmp = int(sys.stdin.readline().rstrip())
#     if tmp <= K:   # 이 부분이 좋았음. 애당초 K보다 큰 동전은 배열에 넣을 필요가 없지. K보다 작은것만 배열에 담음 
#         money.append(tmp)


# count = 0
# for i in range(len(money)-1, -1, -1):
#     count += K//money[i]
#     K -= (K//money[i])*money[i]

# sys.stdout.write(f'{count}')