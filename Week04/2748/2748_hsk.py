import sys
from collections import deque
sys.stdin = open("input.txt","r")
# 01. https://www.acmicpc.net/problem/2748 : 피보나치 수 2

# 
n = int(input())

# 재귀 시간초과
# count1 = 0
# cc = 0
# def fibonacci(x):
#     if x < 3:
#         return 1
    
#     return fibonacci(x-1) + fibonacci(x-2)

# for i in range(1,n+1):
#     a = fibonacci(i)

# print(a)

#----------
# 답1(이게 아주 쪼금 더 빠름)
fibonacci = []
num = 0
for i in range(n+1):
    if i == 0:
        num = 0
    elif i <= 2:
        num = 1
    else:
        num = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(num)
print(fibonacci[-1])
#-------------
# 답 2
dp = [0] * (n+1)
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[-1])