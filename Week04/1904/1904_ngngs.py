import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/week04_Baekjoon/SW_Jungle_5B/input.txt","r")
sys.setrecursionlimit(10**9)
n = int(input())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for i in range(3, n+1) :
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[n])
