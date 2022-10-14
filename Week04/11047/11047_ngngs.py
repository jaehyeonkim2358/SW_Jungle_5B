import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/week04_Baekjoon/SW_Jungle_5B/input.txt","r")

def coin_func(k) :
    global cnt
    cnt = 0
    for i in coin :
        cnt += k//i
        k = k % i


n, k = map(int, sys.stdin.readline().strip().split())
# print(n, k)

coin_list = [int(sys.stdin.readline().strip()) for _ in range(n)]
# print(coin_list)

coin = [x for x in coin_list if x <= k]
coin.sort(reverse=True)
# print(coin)
coin_func(k)
print(cnt)