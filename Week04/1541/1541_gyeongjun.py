import sys
input = sys.stdin.readline().strip

n = input().split('-')
num = []
for arr in n:
    cnt = 0
    s = arr.split('+')
    for n in s:
        cnt += int(n)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)