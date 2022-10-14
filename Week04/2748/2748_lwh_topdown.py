import sys
sys.stdin = open('Week04/2748/2748_lwh.txt', 'r')
input = sys.stdin.readline

n = int(input())

a = [0] * 91
a[1], a[2] = 1, 1

# top down

def fibo(n):

    if a[n]:
        return a[n]
    
    a[n] = fibo(n - 1) + fibo(n - 2)
    return a[n]

print(fibo(n))