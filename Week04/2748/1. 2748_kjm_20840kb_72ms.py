# 메모리랑, 시간 적을 것
# https://www.acmicpc.net/problem/2748

# 재귀로 들어가면 시간 복잡도가 몇인지?? n^2인가?
# https://blog.naver.com/ndb796/221233570962 
# 이거보면 왜 n^2인지 그리고 왜 재귀가 구린 상황이 발생할 수 있는지 나옴.

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
