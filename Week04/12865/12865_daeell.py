import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 기본적인 문제 해결의 방식은 다음과 같다.
# 1. 각 무게를 초과하지 않는 선에서 물건을 담는다.
# 2. 물건을 넣었을 때의 가치가 물건을 넣지 않았을 때의 가치와 비교해서 더 높은 가치를 삽입힌다.
# 3. 해당 문제를 점화식으로 표현하면 다음과 같다.
# 4. 물품번호를 i 배낭의 무게를 j 물건의 무게 리스트를 w 물건의 가치 리스트를 v라 할 때.
# 5. dp[j] = max(dp[j - w[i]] + v[i], dp[j])
# 해당 점화식에 대한 자세한 해석과 적용은 다음과 같이 진행하였다.
total_n, total_w = map(int, input().split())
# 전체 물건의
dp = {i: 0 for i in range(total_w + 1)}
# 각 무게에 따른 최대 가치를 담아주기 위해 다음과 같이 dp테이블을 설정한다.
# 나는 해당 문제를 접근할 때 무게와 가치를 같은 배열에 담아야한다고 생각했는데 점화식 대로 처리하기 위해서 위와같이 값을 저장하는 것이 좋을 것이라고 생각한다.
items = []
for _ in range(total_n):
    weight, value = map(int, input().split())
    items.append((weight, value))

for item in items:
    w, v = item
    for j in range(total_w, w-1, -1):
        dp[j] = max(dp[j-w]+v, dp[j])

print(dp[total_w])
