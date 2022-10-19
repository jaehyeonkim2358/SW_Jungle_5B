import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/week04_Baekjoon/SW_Jungle_5B/input.txt","r")

n = int(input())

num_list = list(map(int, sys.stdin.readline().strip().split()))

dp = [num_list[0]]
for i in range(len(num_list) - 1):
    dp.append(max(dp[i] + num_list[i + 1], num_list[i + 1]))
print(max(dp))