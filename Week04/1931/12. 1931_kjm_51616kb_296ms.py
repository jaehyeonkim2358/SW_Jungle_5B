# https://www.acmicpc.net/problem/1931
# 끝나는 시간이 가장 짧은 기준으로 뽑으면 가장 많은 회의를 담을 수 있대.

import sys
input = sys.stdin.readline
N = int(input())

course = []
for i in range(N):
  course.append(tuple(map(int, input().split())))
# print(course)

# 끝나는 시간이 빠른 순서대로 sorting해야하는데..
# course.sort(key = lambda x: (x[1]))
# 로만 하면 틀림. 반례 주면 
# [ (1, 4), (3, 5), (0, 6), (7,7), (5, 7) ]
# 정렬된 결과 7,7과 5,7을 보면 7이 같기 때문에 (5,7), (7,7) 순서로 오지 않고 그냥 (7,7), (5,7)로 놔뒀는데
# 이러면 (5,7), (7,7)로 짰으면 강의하나 더 추가할 수 있는 기회를 놓치게 된다.
# 따라서 7,7처럼 뒤에 자리가 같을 때는 첫째자리 크기로 정렬한다는 조건을 추가해줘야함.
course.sort(key = lambda x: (x[1], x[0]))




L =[course[0]]  #강의시간이 가장 짧은 놈은 일단 L에 넣어(무조건 선택될테니까)
for i in range(1, len(course)):
  if course[i][0] >= L[-1][1]: #i번째 강의의 시작시간이 L가장 최근에 넣은 강의의 끝시간보다 더 커야만 L에 넣어줌.
    L.append(course[i])
print(len(L))

