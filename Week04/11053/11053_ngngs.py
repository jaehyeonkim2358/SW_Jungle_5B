from array import array
import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/week04_Baekjoon/SW_Jungle_5B/input.txt","r")

#### 이 말 이해하면 이해한 거임
# "이전에 나온 숫자들 중에서 , 현재 값보다 작은 값 중에서, 가지고 있는 부분 수열의 길이 중 
#  가장 긴 부분 수열의 길이에 + 1을 한 값이 현재 값에서 발생할 수 있는 가장 긴 증가하는 부분 수열의 길이가 된다."


n = int(input())
# print(n)

arr_list = list(map(int, sys.stdin.readline().strip().split()))
# print(arr_list)


def longest_increasing_array() :
    global dp
    dp = [0 for _ in range(n)]
    for i in range(n) :
        for j in range(i) :
            if arr_list[i] > arr_list[j] and dp[i] < dp[j]  :
                dp[i] = dp[j]
        dp[i] += 1

longest_increasing_array()
print(max(dp))