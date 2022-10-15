import sys
sys.stdin = open("W03-W04/Week04/9084/input.txt","r")

# for _ in range(int(input())):
#     input()
#     coins = map(int, sys.stdin.readline().split())
#     k = int(input())
#     d = [1] + [0]*k
#     for coin in coins:                  # 동전은 오름차순으로 정렬 되어있다. 가장 작은 동전부터 시작해야 모든 경우의 수가 구해질 수 있다.
#         for x in range(coin,k+1):       #
#             d[x] = d[x] + d[x-coin]     # 우항의 d[x]에는 이전 크기 동전까지의 (해당 인덱스의) 모든 경우의 수가 저장되어 있다. 
#                                         # 좌항에 그대로 d[x]가 있는 것에서 보이듯, 지금 갱신될(현재의 동전 경우의 수가 더해질) 저장소이다.
#                                         # 우항의 d[x-coin]에는 현재 동전까지의, x-coin 인덱스에 해당하는 경우의 수가 저장되어 있다.
#                                         # 인덱스에 해당하는 값은 인덱스 숫자를 전체 가격으로 했을 때 구성할 수 있는 총 경우의 수를 의미한다.
#                                         # 현재 동전 하나는 무조건 추가할테니, 나머지의 경우의 수를 가져오라는 것이 d[x-coin]을 부르는 이유이다.
#                                         #
#                                         # 왜 '현재'동전을 '하나'만 추가하는 것일까.
#                                         # 일단 이전 동전까지의 모오든 경우의 수는 계산이 된 상태이니 차치하고,
#                                         # 현재 동전을 하나만 넣는 이유는 두개 넣는 것 부터는 이전에 다 계산이 되었기 때문이다.
#                                         # d[x-coin-coin]을 생각해 보면 이미 앞에서 처리가 되어있다.
#                                         # 자세히는 x-coin의 지점에서 동전을 하나만 넣고 나머지를 불러오는 행위: d[x-coin-coin]을 이미 했기 때문이다.
#                                         # 현재 배열의 x인덱스를 기준으로 x이후에는 이전 동전까지의 모든 경우의 수가 다 들어있는 것이고,
#                                         # x이전에는 현재 동전까지의 경우의 수가 계산되어 저장되어 있는 상태로 지금의 x까지 온 것이다.
#     print(d[k])


for _ in range(int(input())):
    n = int(input())
    coins = list(map(int, sys.stdin.readline().split()))
    k = int(input())
    d = [[1] + [0]*k for _ in range(n+1)]
    for i,coin in enumerate(coins): 
        for x in range(coin,k+1):       
            d[i+1][x] = d[i][x] + d[i+1][x-coin]
                                       
    print(d[-1][k])