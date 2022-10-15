from sqlite3 import Row
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 기본적인 점화식은 다음과 같이 진행된다.
# dp[start][end] = min(dp[start][end] , dp[start][k] + dp[k+1][end] + d[start]*d[k]*d[end])
# 행렬의 곱은 결합법칙이 성립한다. (a*b)c = a(b*c)가 성립한다. 다만 연산의 수가 달라질 뿐이다.
# 이러한 특성을 이용해서 괄호를 씌우는 역할을 행렬을 따로 계산하는 방식으로 생각하는 것이다.
# (a*b)*c는 dp[1][2] + dp[3][3] + 구분한 두 행렬의 곱 연산의 수가 될 것이다.
# 이게 무슨 의미냐면 a*b가 d라는 행렬이 되었다고 생각하면 d와 c를 또 연산하면서 연산하는 수가 증가할 것이다.
# 그렇기 때문에 기존에 누적된 곱연산을 통해 합쳐진 두 행렬의 곱연산의 수를 더해주는 것이다.

n = int(input())
matrices = [0]+[list(map(int, input().split())) for _ in range(n)]
# 행렬을 입력받는다.
dp = [[0] * (n+1) for _ in range(n+1)]

for gap in range(1, n+1):
    for start in range(1, n-gap+1):
        end = start + gap
        dp[start][end] = sys.maxsize
        for k in range(start, end):
            dp[start][end] = min(dp[start][end], dp[start][k] + dp[k+1]
                                 [end] + matrices[start][0] * matrices[k][1] * matrices[end][1])

print(dp[1][-1])
