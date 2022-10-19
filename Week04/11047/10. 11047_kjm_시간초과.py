import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
for i in range(N):
    input_data=int(input())
    if input_data <= K:
        coins.append(input_data)

coins.sort(reverse=True)

# 코드를 보면 4200에서 1000을 한번에 4번 빼면 되는데 1000원 빼고 또 1000원 빼고 이런식으로 같은 행위를 4번을
# 하거든? 그래서 시간 초과가 뜨는 듯. 그냥 4200//1000하면 한번에 4 갈 수 있는데
count = 0
for coin in coins:
    if K != 0:    
        while K>=coin:
            K = K-coin
            count+=1
    else:
        break
print(count)

# # 한번에 4가는 방식으로 구현
# count = 0
# for coin in coins:
#   while K != 0:
#     if K >= coin:
#       coin_count= K//coin
#       count = count + (coin_count)
#       K-=coin*coin_count
#     break
  
# print(count)