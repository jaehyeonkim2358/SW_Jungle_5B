# 재귀가 깊숙히 들어가면서 stack이 많이 쌓이고 메모리 초과가 뜨게됨.
# 첫 생각이 재귀로 들긴 할텐데.. 
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
