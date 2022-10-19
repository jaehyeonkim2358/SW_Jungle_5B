import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/week04_Baekjoon/SW_Jungle_5B/input.txt","r")

n = int(input())
time_list = list(map(int, sys.stdin.readline().strip().split()))
# print(n, time_list)

time_list.sort()

ans = 0
sum = 0
for time in time_list :
    sum = sum + time
    ans += sum
print(ans)