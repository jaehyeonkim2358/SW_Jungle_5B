import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/week04_Baekjoon/SW_Jungle_5B/input.txt","r")

n = int(input())
# print(n)

dp = [0] * 91
# print(dp)
dp[1] = 1
dp[2] = 1

for i in range(3, 91) :
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])

   