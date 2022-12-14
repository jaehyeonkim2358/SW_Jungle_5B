# 42104KB 4248ms
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

dp = {i: 0 for i in range(total_w + 1)}
# 각 무게에 따른 최대 가치를 담아주기 위해 다음과 같이 dp테이블을 설정한다.

items = []
# 각 아이템의 weight와 value를 보관하기 위한 array 선언
for _ in range(total_n):
    weight, value = map(int, input().split())
    items.append((weight, value))
# 각 weight와 value를 배열에 삽입한다.
# 위와 같이 하는 이유는 추후 반복문을 실행할 때 동일 항목의 무게와 가치를 불러오기 위함이다
for item in items:
    # 아이템 리스트의 무게와 배열을 불러온다.
    w, v = item
    # n번 항목의 무게와 가치를 불러온다.
    # 예제 입력란을 예로 들면 1번째 반복문에서 불러와지는 항목은 (6, 13)이 될 것이다. 이는 해당 item의 무게가 6 value가 13이 됨을 의미한다.
    for j in range(w, total_w+1):
        # 배열을 맨 끝부터 거꾸로 배열을 불러온다.
        dp[j] = max(dp[j-w]+v, dp[j])
        # 결국 동적프로그램의 핵심은 큰 문제를 작은 문제를 나누어 동일하게 처리할 수 있도록 하는 점화식을 찾는 것이며,
        # 점화식을 세우기 위한 방법으로는 문제에 대한 귀납적인 사고를 해내는 것이다.
        # 본 점화식의 목적은 결국 해당 물건을 넣는 것과 넣지 않는 것을 선택해야하는 것이다.
        # 일례로 들어 예제에서 1번 2번 항목을 넣고 3번 항목을 넣는다고 가정하여 보자.
        # 3번 항목을 넣다 보면 dp[3]부터 물건이 들어가게 될 것이다. 그래서 해당 무게 이상 부터 짐을 넣는 것이다.
        # dp[7]이 되었을 때 특별한 점이 나오는데, 이전까지의 dp[7]의 값은 13이었을 것이다 1번 항목이 무게가 6, 값이 13이었기 때문에 이전까지 최고 값이었기 때문이다.
        # 여기서 점화식의 의미가 생긴다. 그러면 7무게의 배낭에서 3번항목을 빼면 4무게의 배낭이 될 것이다. 4무게의 배낭에서 가장 효율적인 선택은 dp[4]로 4번 항목만 들어간 8이 최고의 가치가 된다. 이런 상태에서 우리가 3번항목을 넣을 수 있는 상황에서 6의 가치를 더하면 14의 가치를 얻게 되는 상황에서 13을 가치를 가지고 있는 것 보다 더 나은 선택이 되는 것이다.
        # 그렇게 최고값을 비교해서 교체하여주는 것이다.
print(dp[total_w])
