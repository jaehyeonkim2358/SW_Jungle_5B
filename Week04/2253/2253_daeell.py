# 68916kb 844ms
import sys
from math import sqrt
sys.stdin = open('input2.txt', 'r')
input = sys.stdin.readline

# 최소 점프 횟수를 구한다.
# 일단 최대로 가능한 점프의 길이는 (2*n) ** 0.5 + 1이다. >> 0.5제곱 즉 루트를 사용하게 되면 소숫점이 나올 수 있음. 이것을 int로 변환하면 내림이 발생하여 값이 적어짐. 그래서 +1을 함.
total_, small_ = map(int, input().split())
dp = [[sys.maxsize] * (int(sqrt((2*total_))) + 2) for _ in range(total_+1)]
# 일단 최대로 가능한 점프의 길이는 (2*n) ** 0.5 + 1에다 1을 더 하는 이유는 인덱스를 맞춰주기 위해
# sys.maxsize로 하는 이유는 최솟값으로 갱신해주기 위해서 가장 큰 값을 최솟값으로


def jjuummpp():
    dp[1][0] = 0
    # 첫 번째 돌에서 시작하기 때문에 0에서 초기화
    small_list = set()
    for _ in range(small_):
        small_list.add(int(input()))
    # 돌을 넣어준다.

    for i in range(2, total_+1):
        # 2개 이상 돌이 있으면 일단 무조건 2번 돌까진 간다.
        # 목적지인 돌
        if i in small_list:
            # 작은 돌이니까 갈 수 없음.
            continue
        for v in range(1, int(sqrt(2*total_))+1):
            dp[i][v] = min(dp[i-v][v-1], dp[i-v][v], dp[i-v][v+1])+1
            # i번째인 돈이 v의 속도로 들어오는 경우는 다음과 같다.
            # 1. 속도를 감속해서 오는 것
            # 2. 속도를 유지한 상태에서 오는 것
            # 3. 속도를 증가시켜서 오는 것
    if min(dp[total_]) == sys.maxsize:
        print(-1)
    else:
        print(min(dp[total_]))


jjuummpp()
