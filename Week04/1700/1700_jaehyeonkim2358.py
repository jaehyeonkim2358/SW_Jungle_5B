import sys
from collections import defaultdict, deque


n, k = map(int, sys.stdin.readline().split())       # n: 멀티탭 구멍 수, k: 전체 사용 횟수 (A의 길이)
A = list(map(int, sys.stdin.readline().split()))    # A: 가전의 사용 순서 (길이 = k, 1 <= 가전 번호 <= k)


usage_order = defaultdict(deque)                    # 각 전기용품 번호를 index로 하고, 남은 사용 순(A에서의 index)를 deque([])로 저장한다.
for i in range(len(A)):
    usage_order[A[i]].append(i)
################ 예시 ################
# input:
# 2 5
# 1 2 3 2 1
#
# usage_order:
# usage_order[1] == deque([0, 4])
# usage_order[2] == deque([1, 3])
# usage_order[3] == deque([2])
#####################################


ans = 0
multitap = []
for a in A:
    usage_order[a].popleft()

    # 이미 멀티탭에 꽂힌 물건인 경우
    if a in multitap:
        continue
    # 그 외, 멀티탭에 공간이 남은 경우
    elif len(multitap) < n:
        multitap.append(a)
    # 멀티탭에 꽂힌 물건도 아니고, 멀티탭에 공간도 없는 경우
    else:
        # 멀티탭에 꽂힌 물건 중, 다음 사용이 가장 늦는 물건을 뽑는다.
        max_order_idx = -1
        target = -1
        for j in range(len(multitap)):
            if usage_order[multitap[j]]:
                if max_order_idx < usage_order[multitap[j]][0]:
                    max_order_idx = usage_order[multitap[j]][0]
                    target = j
            else:   # 남은 사용 순서가 없는 물건(이제 사용 안하는 물건)은 바로 뽑아도 됨
                target = j
                break
        multitap[target] = a
        ans += 1

sys.stdout.write(f'{ans}')