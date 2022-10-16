# 동전 0

import sys

n, k = map(int, sys.stdin.readline().split())
coin_list = [int(sys.stdin.readline().strip()) for _ in range(n)]


#for _ in range(n):
#    coin_list.append(int(sys.stdin.readline()))

def min_coin_count(value, coin_list):
    count = 0
    coin_list.reverse()

    for coin in coin_list:
        if value >= coin:
            count += value // coin
            value = value % coin
    
    return count
    
    
print(min_coin_count(k, coin_list))
