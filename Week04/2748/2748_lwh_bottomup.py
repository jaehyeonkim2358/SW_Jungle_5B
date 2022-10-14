import sys
sys.stdin = open('Week04/2748/2748_lwh.txt', 'r')
input = sys.stdin.readline

n = int(input())

a = [0] * 91
a[1], a[2] = 1, 1

# bottom up

def fibo(n):
    if n <= 2:
        return a[n]
    for m in range(3, n+1):
        a[m] = a[m-1] + a[m-2]
    
    return a[n]

print(fibo(n))