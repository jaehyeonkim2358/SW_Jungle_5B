import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/week04_Baekjoon/SW_Jungle_5B/input.txt","r")

N = int(input())
dis_list = list(map(int, sys.stdin.readline().strip().split()))
# print(dis_list)

wage_list = list(map(int, sys.stdin.readline().strip().split()))
# print(wage_list)

wage = wage_list[0]
sum = 0
for i in range(N-1) :
    sum += wage * dis_list[i]
    if wage > wage_list[i+1] :
        wage = wage_list[i+1]

print(sum)