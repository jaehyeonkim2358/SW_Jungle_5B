import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/week04_Baekjoon/SW_Jungle_5B/input.txt","r")

t = int(input())
for _ in range(t) :
    k = int(input())
    n = int(input())
    # print(t,k,n)
    dp = [[0] * 15 for _ in range(15)]
    # print(dp)
    for i in range(15) :
        dp[0][i] = i
        dp[i][1] = 1
    # print(dp)
    for i in range(1, 15) :
        for j in range(2, 15) :
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
    print(dp[k][n])