# 신입 사원
import sys 
input = sys.stdin.readline
print = sys.stdout.write
T = int(input())
for _ in range(T):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(tuple(map(int, input().split(' '))))
    arr.sort()

    cnt = 1
    maxTwo = arr[0][1]
    for one, two in arr:
        if two < maxTwo:
            cnt += 1
            maxTwo = two
    print(f'{cnt}\n')