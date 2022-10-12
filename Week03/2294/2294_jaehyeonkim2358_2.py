# DP 풀이

import sys


n, k = map(int, sys.stdin.readline().split())
coin_list = []
for _ in range(n):
    tmp = int(sys.stdin.readline().rstrip())
    # 목표 금액(k)보다 큰 값을 가지는 동전은 리스트에 저장하지 않는다.
    if tmp <= k:
        coin_list.append(tmp)


INF = 10002                 # k의 입력범위보다 큰 값. 리스트 초기화 및 갱신 여부 체크를 위한 변수
cost = [INF] * (k+1)        # 금액을 index로 하고 해당 금액을 만들 수 있는 최소 동전의 개수를 저장하는 리스트


# 입력된 동전을 순회
for i in range(len(coin_list)):
    current_cost = coin_list[i]
    cost[current_cost] = 1          # 현재 동전으로 만들 수 있는 금액은 동전 1개로 만들 수 있음
    # 현재 동전으로 [현재 동전의 금액 ~ k원] 까지 만들어보자!
    for j in range(current_cost, k+1, 1):
        # 기존에 저장된 각 금액에 대한 동전 개수의 최소값을
        # 현재 동전으로 만드는 경우와 비교하여 갱신
        cost[j] = min(cost[j], cost[j-current_cost]+1)


# k원을 만들지 못한 경우
if cost[k] == INF:
    sys.stdout.write('-1')
# 그 외의 경우
else:
    sys.stdout.write(f'{cost[k]}')