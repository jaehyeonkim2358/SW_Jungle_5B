# Top-Down

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())

count=0
def recursion(n):
    if n == 1:
        count = 1
    elif n ==2:
        count = 2
    else:
        count = recursion(n-1) + recursion(n-2)
    return count
print(recursion(n))
