# 11047: 동전 0
# 준규 동전 N 종류, 동전 활용해서 합 K로 만들라고 함. 동전 개수의 최솟값?

import sys
sys.stdin = open("11047/input.txt","r")
input = sys.stdin.readline
N, K = map(int, input().split())
coins = [int(input().rstrip()) for _ in range(N)]
answer = 0 # 답을 저장시킬 곳을 만들어줘야함.
# 우리가 구하고자 하는 것이 필요한 동전의 최소 갯수이다.
# 가치의 합 K가 1억까지이기 때문에 dp처럼 배열에 저장시켜 메모이제이션을 하게 되면 1억번의 반복으로 시간초과가 발생할 것이다.
# 거스름돈 걸러준다고 생각하면 4200 = 1000 * 4 + 100 * 2이니깐 
# 해당 합보다 거스름돈이 크면 안 되기 때문에 큰 가치의 동전을 먼저 써서 확인한다.
# 범위가 제한적이기 때문에 for문을 활용하고, 오름차순으로 정렬되어있는 coins를 내림으로 활용한다.
# 큰 가치의 값부터 비교하여 동전이 가치의 합 보다 크면 continue
# 가치의 합을 해당 동전으로 나눈 몫의 합이 결론적으로 구하고자 하는 값이므로 
# for문을 통해서 몫을 구하고, 나머지가 0이 아닌 경우 K의 합에서 구한 몫과 동전을 빼준다. 

for i in range(len(coins)-1, -1, -1):
    if coins[i] > K: continue
    q = K // coins[i]
    r = K % coins[i]
    answer += q
    if r == 0: break
    else: K -= q * coins[i]

print(answer)