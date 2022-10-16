# 1931: 회의실 배정
# 한 개의 회의실 => N개의 회의

import sys
sys.stdin = open("1931/input.txt","r")
input = sys.stdin.readline

N = int(input().rstrip())
meetings = [list(map(int, input().split())) for _ in range(N)]
# 끝 시간을 기준으로 오름차순 정렬, 끝 시간이 같으면 시작 시간으로 오름차순 정렬
# 왜냐하면 회의가 빨리 끝날 수록 회의를 더 많이 할 수 있을 가능성 높음
# 정렬하는 기준을 잡을 때 x[1]을 기준으로 오름차순 정렬을 하고, 다시 그 정렬에서 x[0]를 기준으로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

count, end = 0, 0
for meeting in meetings:
    if int(meeting[0]) >= end:
        count += 1
        end = int(meeting[1])

print(count)