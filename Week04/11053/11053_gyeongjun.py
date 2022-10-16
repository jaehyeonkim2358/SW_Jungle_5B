import sys
input = sys.stdin.readline
n = int(input())
a = [0] + list(map(int, input().split()))
num = a[0]
cnt = 0
for i in range(1, n+1):
    if(a[i] > num):
        cnt += 1
        num = a[i]
print(cnt)