import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/week04_Baekjoon/SW_Jungle_5B/input.txt","r")

n = int(input())

def fib(n) :
    global recur_cnt
    recur_cnt += 1
    if n == 1 or n == 2:
        recur_cnt -= 1
        return 1
    else :
        return (fib(n-1) + fib(n-2))

def fibonacci(n) :
    global dp_cnt
    dp[1] = 1
    dp[2] = 1 
    for i in range(3, n+1) :
        dp[i] = dp[i-1] + dp[i-2]
        dp_cnt += 1
    return dp[n]

recur_cnt = 0

dp_cnt = 0
dp = [0] * 41



fib(n)
fibonacci(n)
print(recur_cnt+1, dp_cnt)