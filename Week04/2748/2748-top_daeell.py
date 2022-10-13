import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())

d = [0] * (n+1)


def fibo(x):
    if x == 0:
        return 0
    elif x == 1 or x == 2:
        # i가 1이나 2면 바로 return
        d[x] = 1
        return d[x]
    elif d[x] != 0:
        return d[x]
        # 값이 저장되어 있는 경우 값을 출력함.
    else:
        d[x] = fibo(x-2) + fibo(x-1)
        return d[x]
        # 값이 저장되어 있지 않은 경우 값을 저장함. (메모이제이션)


print(fibo(n))
