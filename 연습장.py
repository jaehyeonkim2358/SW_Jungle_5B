import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
for i in range(N):
    input_data=int(input())
    if input_data <= K:
        coins.append(input_data)
coins.sort(reverse=True)

count = 0
for coin in coins:
    if K != 0:    
        while K>=coin:
            K = K-coin
            count+=1
    else:
        break
print(count)