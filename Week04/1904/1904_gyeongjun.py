import sys
input = sys.stdin.readline

n = int(input())
fibo = [0] * 1000001

fibo[1] = 1
fibo[2] = 2

for k in range(3,n+1):
    fibo[k] = (fibo[k-1]+ fibo[k-2])%15746
print(fibo[n])