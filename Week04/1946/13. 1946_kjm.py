# https://www.acmicpc.net/problem/1946

import sys
input = sys.stdin.readline


T=int(input())
for _ in range(T):
  people=[]
  N = int(input())
  for _ in range(N):
    people.append(list(map(int, input().split())))
  people.sort()
  # [[1, 4], [2, 5], [3, 6], [4, 2], [5, 7], [6, 1], [7, 3]]
  temp = people[0][1] #(1,4)에서 4임.
  cnt =1

  for j in range(len(people)):
    target = people[j][1]
    if temp > target:
      cnt +=1
      temp = target #왜 이짓을 하냐?? (이짓을 안하면 계속 1,4만 보게 됨..)
  print(cnt)


    