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