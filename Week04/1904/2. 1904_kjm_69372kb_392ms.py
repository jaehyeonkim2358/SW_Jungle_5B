# https://www.acmicpc.net/problem/1904
# https://kils-log-of-develop.tistory.com/244 정리 굿
import sys
input = sys.stdin.readline
n = int(input())

# dp = [0]* (n+1) #런타임 에러 뜬 원인(N) N이 백만까지니까 딱 백만만 넣으면 안되고 좀 넉넉히 넣어줘야함.
dp = [0]* (10000100)
dp[1] = 1
dp[2] = 2
# dp[3] = 3 
# dp[4] = 5
# dp[5] = 8
# 설마 피보나치? #이렇게 귀납적으로 넣어보면서 패턴을 찾는 것도 방법임
for i in range(3, n+1):
    dp[i] = (dp[i-2]+dp[i-1])%15746
print(dp[n])


# 재현이 코드 리뷰

# import sys
# sys.setrecursionlimit(10**9)

# T = 15746
# N = int(sys.stdin.readline().rstrip())

# fibo_num = [2, 1]

# def fibonacci(x):
#     for i in range(3, x+1):
#         fibo_num[i%2] = (fibo_num[0]%T + fibo_num[1]%T)%T
#         # 나는 애당초 dp = [0]* (10000100) 이 부분에서 백만개 길이의 배열을 만들고 시작했다면..
#         # 재현이는 딱 길이 2짜리 배열만 만들어서 문제를 품
#         # fibo_num[i%2] = 이부분에서 홀짝 여부를 묻고, 만약 짝수면 fibo_num의 0번째 인자를 손대고, 홀수이면 1번째 인자를 손댐
#         # 그럼 어케 손을 대냐? -> 이 전까지 계산한 fibo_num을 더해서
#         # 뭔말인고하니.. 1 2 3 5... 피보나치 수열에서 3번째 숫자가 궁금하면? 
#         # 3번째의 3은 홀수니까 fibo =[2,1]이 fibo = [2,3]으로 바뀜.
#         # 그리고 return fibo_num[x%2]에서 3을 출력.
#         # 우리가 필요한건 어차피 구하고자하는 N앞에 있는 2개의 숫자인데 왜 모든 숫자를 배열로 가지고있냐? 라는 컨셉.
#     return fibo_num[x%2]


# print(fibonacci(N))

