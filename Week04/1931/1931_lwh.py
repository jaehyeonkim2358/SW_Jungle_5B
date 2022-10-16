import sys
sys.stdin = open('Week04/1931/1931_lwh.txt', 'r')
input = sys.stdin.readline 

# 철로랑 비슷 

N = int(input())

calls = []
for _ in range(N):
    s, e = map(int, input().split())
    calls.append((s, e))

calls = sorted(calls, key = lambda x : (x[1], x[0]))

end = 0
count = 0
for s, e in calls:
    if s >= end:
        end = e
        count += 1
        
print(count)

