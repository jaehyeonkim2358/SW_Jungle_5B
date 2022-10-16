import sys
sys.stdin = open("input.txt","r")
# 10. https://www.acmicpc.net/problem/11047: 동전 0
input = sys.stdin.readline

n, k = map(int, input().split())

coin_list = []
for _ in range(n):
    coin_list.append(int(input()))

count1 = 0
for i in range(n-1, -1, -1):
    if k == 0:
        break
    while coin_list[i] <= k:
        count1 = count1 + (k // coin_list[i])
        k = k % coin_list[i]
         
print(count1)