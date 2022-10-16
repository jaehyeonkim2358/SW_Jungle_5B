# 회의실 배정
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
meetings = []
for _ in range(N):
    meetings.append(tuple(map(int, input().split(' '))))

meetings.sort(key=lambda x:(x[0], x[1]))
time = meetings[-1][1]
cnt = 0
for meeting in meetings[::-1]:
    if meeting[1] <= time:
        time = meeting[0]
        cnt += 1
print(f'{cnt}')