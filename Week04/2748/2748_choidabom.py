# 2748: 피보나치 수 2
import sys
sys.stdin = open("2748/input.txt","r")
input = sys.stdin.readline

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    fib_arr = [0, 1]
    for i in range(2, n+1):
        num = fib_arr[i-1] + fib_arr[i-2]
        fib_arr.append(num)

    return fib_arr[n]

print(fib(int(input())))