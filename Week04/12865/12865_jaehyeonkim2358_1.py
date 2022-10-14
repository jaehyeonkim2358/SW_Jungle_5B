# Knapsack
import sys


n, k = map(int, sys.stdin.readline().split())

dp = [0] * (k+1)        # 각 무게(index)에서 가질 수 있는 최대 가치를 저장해줄 리스트
for _ in range(n):
    weight, value = map(int, sys.stdin.readline().split())
    if weight <= k:
        # 입력 받은 물건(무게, 가치)을 이용해서 비교한다.
        for weight, value in knapsack:                  
            # "구하려는 무게(k) ~ 현재 물건의 무게(weight)" 범위에서 
            # 각각의 최대 가치합을 현재 물건의 가치(value)를 이용해서 갱신해준다.
            for j in range(k, weight-1, -1):            
                # 'j와 현재 물건의 무게(weight)차 만큼의 무게'가 가지고 있는 최대 가치합에
                # 현재 물건의 가치(value)를 더해준 값과
                # 기존의 무게j에서의 최대 가치합을 비교해준 뒤
                # 둘 중 큰 값으로 갱신한다.
                dp[j] = max(dp[j], value + dp[j - weight])


sys.stdout.write(f'{dp[k]}')