import sys
sys.setrecursionlimit(10**9)

T = 15746
N = int(sys.stdin.readline().rstrip())

fibo_num = [2, 1]

def fibonacci(x):
    for i in range(3, x+1):
        fibo_num[i%2] = (fibo_num[0]%T + fibo_num[1]%T)%T
    return fibo_num[x%2]


print(fibonacci(N))
