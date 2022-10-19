# 32416 88
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
items = deque(map(int, input().split()))
tap = [0] * n
ans = 0

while items:
    if items[0] in tap:
        items.popleft()
    elif 0 in tap:
        # 콘센트의 자리가 있다면.
        tap[tap.index(0)] = items.popleft()
        # 콘센트에 꽂는다.
        # 콘센트에 꽂았으니까 꽂을 리스트에서 제외한다.
    # 콘센트에 자리가 없다면.
    else:
        tap_index = []
        for i in tap:
            if i not in items:
                # 앞으로 뽑을 리스트에 없는 콘센트를 찾는다
                tap_index.append(sys.maxsize)
                break
            else:
                # 꽂혀있는 아이템들이 나중에 쓰일거라면
                # 꽂혀있는 아이템의 index를 비교를 어떻게 하지
                tap_index.append(items.index(i))

        # 인덱스 모아놓은 곳에서 가장 큰 인덱스를 가진 멀티탭을 뽑는다.
        tap[tap_index.index(max(tap_index))] = items.popleft()
        ans += 1

print(ans)
