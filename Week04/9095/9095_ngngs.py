import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/week04_Baekjoon/SW_Jungle_5B/input.txt","r")

t = int(input())
for _ in range(t) :
    n = int(input())
    dp = [0] * 11
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, 11) :
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[n])