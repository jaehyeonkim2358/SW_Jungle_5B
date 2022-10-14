import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/week04_Baekjoon/SW_Jungle_5B/input.txt","r")

n = int(input())

# 연쇄행렬곱셈 https://source-sc.tistory.com/24

# 연쇄행렬곱셈을 만들기 위해 데이터 나눠 받기
nums = list(map(int, input().split()))
for _ in range(n-1):
    _, c = map(int, input().split())    # 이런 식으로 데이터 받는 방법도 연습하자.
    nums.append(c)

# print(nums) 

dp = [[0]*n for _ in range(n)]
for diagonal in range(n) :  # 첫 번째 대각선은 0으로 깔림.
    for i in range(n - diagonal) :
        j = i + diagonal

        if i == j : # (0,0) (1,1) (2,2) 는 그대로 0으로 둠
            continue

        dp[i][j] = float('inf')
        for k in range(i, j) :
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + nums[i] * nums[k+1] * nums[j+1])
            print(dp)
print(dp[0][n-1])
