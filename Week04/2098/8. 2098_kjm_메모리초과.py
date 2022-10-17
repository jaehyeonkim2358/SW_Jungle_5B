# https://www.acmicpc.net/problem/2098
# 순열을 활용해서 풀어보자 ->메모리초과(공간복잡도가 O(n!)이라..도시가 10개면 10! 3,628,800개의 배열이 필요함)


import sys
from itertools import permutations

input = sys.stdin.readline
n = int(input())

w = []
for _ in range(n):
  w.append(list(map(int, input().split())))
# print(w) [[0, 10, 15, 20], [5, 0, 9, 10], [6, 13, 0, 12], [8, 8, 9, 0]]

citys=[]
for i in range(1,n+1):
  citys.append(i)

citys_path = list(permutations(citys))


total_path_list = []
for i in citys_path:
  #처음 출발을 1에서 했으면 4까지 돌고 1로 돌아오는 상황을 표현
  i = [*i]
  i.append(i[0])
  # print(i) [1, 2, 3, 4, 1],[1, 2, 4, 3, 1] ...
  pay_sum = 0
  for j in range(len(i)-1):
    # 1에서 2가는 비용, 2에서 3가는 비용 계산해야함.
    from_city = i[j] 
    to_city = i[j+1]
    if w[from_city-1][to_city-1] ==0:
      break
    else:
      pay_sum = pay_sum + w[from_city-1][to_city-1] #w를 만들때 0부터 인덱싱하게 해서 -1해줘야함
  total_path_list.append(pay_sum)
print(min(total_path_list))