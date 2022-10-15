import sys
sys.stdin = open("W03-W04/Week04/12865/input.txt","r")

n, k = map(int, input().split())

# 아래의 모든 방법은, 현재 선택된 아이템을 안넣은 value와 넣은 value 중에서 큰값을 선택하는 과정.

# 1. dp 테이블을 딕셔너리로 구현.
def go(n,k):    # 함수 안에서 실행하는게 더 빠르다.
    dp = dict({0:0})
    for _ in range(n):
        item_w, item_v = map(int, input().split()) # 현재 아이템 정보.
    
        if item_w <= k:  # 아이템 w가 최종 w보다는 작아야 한다. 최종 w보다 큰 입력값도 있을 수 있다.
            tmp = {}     # 꼭 tmp를 만들어 한번에 업데이트 할 필요는 없지만, 이게 더 빠르다.
            for w, v in dp.items():     # 이미 구해진 결과들을 현재 아이템을 사용해 갱신
                if w + item_w <= k and item_v + v > dp.get(w + item_w, 0):
                    tmp[w+item_w] = v+item_v
            dp.update(tmp)
    return max(dp.values())
print(go(n,k))

# 2. 일차원 배열 덮어쓰기 활용. 단, 배열을 채우는 방향이 오른쪽에서 왼쪽.
# N, K = map(int, input().split())
# WV = [list(map(int, input().split())) for _ in range(N)]
#
# def get_max_value_case(K):
#     dp = [0] * (K + 1)
#     for w, v in WV:
#         for i in range(K, -1, -1):
#             if i-w < 0:
#                 break
#             dp[i] = max(dp[i-w]+v, dp[i])
#
#     return dp[K]
# print(get_max_value_case(K))

# 2-1. (틀림) 일차원 배열 덮어쓰기 활용.
# n, k = map(int, input().split())
# dp = [0]*(k+1)
#
# for _ in range(n):  # i : item number
#     weight, value = map(int, input().split())
#     for c in range(weight,k+1):  # c : capacity
#         dp[c] = max(dp[c], dp[c-weight]+value)  # 배열 왼쪽부터 덮어쓰면서 진행하기 때문에,
#                                                 # 여기서 dp[c-weight]의 값이 현재 아이템에 대해 갱신된 상태이다.
#                                                 # 우리가 필요한건 이전 아이템에 대한 dp[c-weight]인데 말이지.
# print(dp[k])

# 3. 이차원 배열 활용
# n, k = map(int, input().split())
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):  # i : item number
    weight, value = map(int, input().split())
    for c in range(1,k+1):  # c : capacity
        if weight > c:
            dp[i][c] = dp[i-1][c]
        else:
            dp[i][c] = max(dp[i-1][c], dp[i-1][c-weight]+value)

print(dp[-1][k])

# 4. 배열 두개 이용해서 홀짝으로 번갈아 활용하기
# n, k = map(int, input().split())
# dp = [[0]*(k+1)] + [[0]*(k+1)]  # 번갈아 가며 사용.
#
# for i in range(1,n+1):  # i : item number
#     weight, value = map(int, input().split())
#     for c in range(1,k+1):  # c : capacity
#         if weight > c:
#             dp[i%2][c] = dp[i%2-1][c]
#         else:
#             dp[i%2][c] = max(dp[i%2-1][c], dp[i%2-1][c-weight]+value)
#
# print(dp[n%2][k])



