# 메모리랑, 시간 적을 것
# https://www.acmicpc.net/problem/2748
# 재귀로 들어가면 시간 복잡도가 몇인지?? n^2인가?

import sys
input = sys.stdin.readline
n = int(input())

fibo =[]
num = 0

for i in range(n+1):
    if i == 0:
        num =0
    elif i <= 2:
        num = 1
    else:
        num = fibo[-1] + fibo[-2]
    fibo.append(num)
print(fibo[-1])
