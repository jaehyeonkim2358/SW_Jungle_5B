import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/week04_Baekjoon/SW_Jungle_5B/input.txt","r")

n = int(input())
# print(n)

# 출처: https://suri78.tistory.com/26 [공부노트:티스토리]
## 빨리 끝나는 회의 순서대로 정렬을 해야 한다. 이유는 간단하다. 빨리 끝날수록 뒤에서 고려해볼 회의가 많기 때문이다.

"""
단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 
회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.
즉 회의의 시작시간과 끝나는 시간도 같을 수 있다는 것은
2
3 3
3 3
의 input이 주어져도 output은 2가 나와야 한다는 것이다.
"""

## 정렬을 1. 끝나는 시간의 오름차순 2. 시작하는 시간의 오름차순으로 해주어야 한다.

meet_list = [[0] * 2 for _ in range(n)]
for i in range(n) :
    start, end = map(int, sys.stdin.readline().strip().split()) 
    meet_list[i][0] = start
    meet_list[i][1] = end

meet_list.sort(key = lambda x : (x[1], x[0]))

cnt = 1
end_time = meet_list[0][1]
for i in range(1, n) :
    if meet_list[i][0] >= end_time :    # end_time이 뒤에 오는 시작시간보다 빠르다면 cnt += 1
        cnt += 1
        end_time = meet_list[i][1]

print(cnt)