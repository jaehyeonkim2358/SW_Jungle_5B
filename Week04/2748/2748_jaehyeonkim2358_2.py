# Bottom-Up

import sys

n = int(sys.stdin.readline().rstrip())
fibo_num = [0] * (n+2)
fibo_num[1] = 1
fibo_num[2] = 1

def fibonacci(x):
    for i in range(3, x+1):
        fibo_num[i] = fibo_num[i-1] + fibo_num[i-2]
    return fibo_num[x]

sys.stdout.write(f'{fibonacci(n)}')