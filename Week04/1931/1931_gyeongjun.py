import sys
input = sys.stdin.readline

n = int(input())
time_list = []
for _ in range(n):
    s, e = map(int, input().split())
    time_list.append([s, e])

time_list = sorted(time_list, key=lambda x: x[0]) 
# 시작 시간을 기준으로 오름차순
time_list = sorted(time_list, key=lambda x: x[1]) 
# 끝나는 시간을 기준으로 다시 오름차순

last_t = 0
cnt = 0
for start, end in time_list:
    if start >= last_t: # 시작시간이 회의의 마지막 시간보다 크거나 같을경우
        cnt += 1
        last_t = end
print(cnt)