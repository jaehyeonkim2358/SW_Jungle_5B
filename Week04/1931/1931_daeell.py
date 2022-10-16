# 51616 284
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
meeting_list = [tuple(map(int, input().split())) for _ in range(n)]
meeting_list.sort(key=lambda x: (x[1], x[0]))

start = (0, 0)
ans = 0
for meeting in meeting_list:
    if meeting[0] >= start[1]:
        start = meeting
        ans += 1

print(ans)
