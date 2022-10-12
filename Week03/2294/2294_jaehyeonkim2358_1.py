# BFS 풀이

import sys
from heapq import heappop, heappush


n, k = map(int, sys.stdin.readline().split())
coin_list = []
for _ in range(n):
    tmp = int(sys.stdin.readline().rstrip())
    # 목표 금액(k)보다 큰 값을 가지는 동전은 리스트에 저장하지 않는다.
    if tmp <= k:
        coin_list.append((1, tmp))


def solution():
    global k
    visited = [0] * (k+1)
    pq = coin_list[:]
    while pq:
        coin = heappop(pq)
        if coin[1] == k:
            return coin[0]
        # 모든 동전을 순회하며 금액을 만들어줌
        for c in coin_list:
            # k 이하인 금액 이며, 아직 만들어 주지 않은 금액일 경우
            if c[1]+coin[1] <= k and visited[c[1]+coin[1]] == 0:
                visited[c[1]+coin[1]] = 1
                heappush(pq, (coin[0] + c[0], coin[1] + c[1]))
    
    return -1


sys.stdout.write(f'{solution()}')