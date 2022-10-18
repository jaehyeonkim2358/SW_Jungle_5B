# 멀티탭 스케줄링
import sys
input = sys.stdin.readline
print = sys.stdout.write
cnt = 0
N, K = map(int, input().split(' '))
power = [[] for _ in range(K+1)]
itemOrder = list(map(int, input().split(' ')))

for idx, item in enumerate(itemOrder):
    power[item].append(idx)

tap = []
for idx, item in enumerate(itemOrder):
    power[item].pop(0)
    if item in tap:
        continue
    
    if len(tap) < N:
        tap.append(item)
        continue

    t = -1
    v = -1
    for i in tap:
        if not power[i]:
            v = i
            break
        if len(power[i])>=1 and power[i][0] > t:
            t = power[i][0]
            v = i 
    tap.remove(v)
    tap.append(item)
    cnt += 1
    
print(f'{cnt}')