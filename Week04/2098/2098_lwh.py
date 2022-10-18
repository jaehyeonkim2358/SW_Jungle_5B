import sys
sys.stdin = open('Week04/2098/2098_lwh.txt', 'r')
input = sys.stdin.readline

def dfs(u, visited):
    if dp[u][visited]:   # 이미 최소 비용이 계산되어 있다면 그 값 반환 
        return dp[u][visited]
    
    if visited == (1 << N) - 1: # 모든 도시를 방문 했다면 ! (1<<N) - 1 => 11111111 N개 = 2^N - 1
        if W[u][0]:             # 현재 도시(u)-> 마지막 도시에서 출발 도시(0)로 가는 경로가 존재 할 때
            return W[u][0]
        else:                   # 현재 도시(u)-> 마지막 도시에서 출발 도시(0)로 가는 경로가 없을 때
            return INF          

    min_cost = INF

    for v in range(1, N):       # u에서 갈 수 있는 다음 도시들 다 돌기 (출발도시 제외)
        if not W[u][v]:         # u에서 갈 수 없다면 skip    
            continue
        if visited & (1 << v):  # 갔던 곳이면 skip
            continue
        
        # v가 안갔 던 곳이면 -> 'v에서 첫 도시로 돌아가는 비용 + u -> v 로 가는 비용' vs '현재 u에서 첫도시로 돌아갈때 최소 비용이라고 알고 있던 값'   
        min_cost = min(min_cost, dfs(v, visited | (1 << v)) + W[u][v])

    dp[u][visited] = min_cost

    return min_cost

N = int(input())

INF = int(1e9) # 각 edge의 비용 최댓값(1,000,000) * 싸이클에서 간선 수 최댓값 (16) 보다 큰 임의의 값
dp = [[0] * (1 << N) for _ in range(N)] # 비용 최댓값의 배열. 도시 수(N) * 모든경우 방문했을 때의 경로 + 1 (1<<N)

W = [list(map(int, input().split())) for _ in range(N)]

print(dfs(0, 1)) # 0에서 시작. 0번도시 방문체크된 visited = 1

