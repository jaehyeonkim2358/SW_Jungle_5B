# 메모리랑, 시간 적을 것
# https://www.acmicpc.net/problem/2748
# 왜 시간초과??


import sys
input = sys.stdin.readline
n = int(input())

def recursion(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return recursion(n-2) + recursion(n-1)


print(recursion(n))