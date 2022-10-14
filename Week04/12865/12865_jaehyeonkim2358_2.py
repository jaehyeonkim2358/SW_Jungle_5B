# Knapsack
import sys

n, k = map(int, sys.stdin.readline().split())

dp = {0:0}
for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    if w <= k:
        tmp = {}
        for _w, _v in dp.items():
            if _w+w <= k and _v+v > dp.get(_w+w, 0):
                tmp[_w+w] = _v+v
        dp.update(tmp)

sys.stdout.write(f'{max(dp.values())}')