# https://www.acmicpc.net/problem/9084
# 입력
import sys
input = sys.stdin.readline
T = int(input()) #test회수
for i in range(T):
  N = int(input()) #동전 가지 수 
  coins = list(map(int, input().split()))
  coins.sort(reverse=True)
  M = int(input()) #동전으로 만들어야하는 금액 
  # print(coins)
  
