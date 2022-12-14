import sys
sys.stdin = open("W03-W04/Week04/2098/input.txt","r")

n = int(input())
w = [] 
for _ in range(n):
    w.append(list(map(int, sys.stdin.readline().split())))
dp = [[-1] * (1<<(n-1)) for _ in range(n)]  # 어차피 시작 정점의 이진수 자리는 항상 1이기 때문에 한칸 줄여서.
                                            # n-1개의 bit로 만들 수 있는 경우의 수는 1<<(n-1).
                                            # 각각의 경우의 수에대한 십진수 i는  0 <= i <= 1<<(n-1) - 1
                                            # 그래서 함수 호출시 모두 포함하는 경우에 대한 십진수를 1<<(n-1) - 1 로 준다.
def go(i, included):
    if dp[i][included] > 0:          # 지금 호출에 대해서 dp테이블에 값 있다면 그걸 반환하면 됨.    
                                     # 이 조건을 아래 not included and w[i][0] 뒤에 둔다면, 맨 마지막 단위에서 참조할 수 있는 경우가 무시됨.
                                     # 정점이 4개인 문제의 예제가 바로 이 경우 해당.
        print(f'dp is referenced at {i} : {bin(included)[2:].zfill(n-1)}')
        return dp[i][included]
    
    if not included and w[i][0]:     # v_i, {}
        dp[i][included] = w[i][0]
        return w[i][0]
    
    min_ = sys.maxsize
    for j in range(1,n):
        if included & (1<<(j-1)) and w[i][j]:
            length = w[i][j] + go(j, included - (1<<(j-1)))
            if length < min_ : min_ = length
            
    dp[i][included] = min_
    
    return dp[i][included]

# go(0, (1<<(n-1))-1)
# print(dp[0][(1<<(n-1))-1])

# dp테이블 대신 캐시 데코레이터 활용.
# import functools
# n = int(input())
# w = [] 
# for _ in range(n):
#     w.append(list(map(int, sys.stdin.readline().split())))

# @functools.lru_cache(maxsize = sys.maxsize)
# def go(i, included):  
#     if not included and w[i][0]:     # v_i, {}
#         return w[i][0]
    
#     min_ = sys.maxsize
#     for j in range(1,n):
#         if included & (1<<(j-1)) and w[i][j]:
#             length = w[i][j] + go(j, included - (1<<(j-1)))
#             if length < min_ : min_ = length
            
#     return min_


# print(go(0, (1<<(n-1))-1))
# print(go.cache_info())

# visited만 비트마스킹을 사용한 완전탐색. dp테이블을 전혀 참조하지 않는다. 삽질.
# def go(n, i, visited):
#     if visited == (1 << n) - 1:
#         return 0
     
#     if dp[i][visited] != -1:
#         return dp[i][visited]
#     else:
#         # visited += 1 << i
#         tmp = float('inf')
#         for j in range(1,n):
#             nv = 1 << j 
#             if w[i][j] and not nv & visited:
#                 cost = w[i][j] + go(n, j, visited+nv)
#                 if cost < tmp: tmp = cost
        
#         dp[i][visited] = int(tmp)
#         return tmp

# print(go(n,0,1))