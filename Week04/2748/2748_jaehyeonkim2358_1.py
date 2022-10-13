# Top-Down

import sys

n = int(sys.stdin.readline().rstrip())
fibo_num = [0] * (n+2)
fibo_num[1] = 1
fibo_num[2] = 1

def fibonacci(x):
    if fibo_num[x] != 0:
        return fibo_num[x]
    for i in range(x, 2, -1):
        fibo_num[i] = fibonacci(i-1) + fibonacci(i-2)
    return fibo_num[x]

sys.stdout.write(f'{fibonacci(n)}')