import sys

# 끝시간을 기준으로 오름차순 정렬, 끝시간이 같으면 시작 시간으로 오름차순 정렬

n = int(sys.stdin.readline().rstrip())
time = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(n)], key= lambda x: (x[1], x[0]))

end = 0
count = 0
for s, e in time:
    if end <= s:
        end = e
        count += 1

sys.stdout.write(f'{count}')