import sys

# 시작시간을 기준으로 오름차순 정렬, 시작시간이 같으면 끝시간으로 오름차순 정렬

n = int(sys.stdin.readline().rstrip())
time = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(n)], key= lambda x: (x[0], x[1]))

# 회의실이 예약된 마지막시간부터 첫시간 순으로 탐색
start = time[-1][1]
count = 0
for s, e in time[::-1]:
    if start >= e:
        start = s
        count += 1

sys.stdout.write(f'{count}')