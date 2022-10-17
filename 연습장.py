# 외판원 순회 # 남 코드 그대~~~로 복사
import sys
input = sys.stdin.readline
n = int(input())

INF = sys.maxsize
dp = [[INF] * (1 << n) for _ in range(n)]


def dfs(x, visited): #x는 출발하는 도시 (결국 x로 돌아와야함..), visitied는 방문한 도시
    if visited == (1 << n) - 1:     # 모든 도시를 방문했다면
        if graph[x][0]:             # 출발점으로 가는 경로가 있을 때
            return graph[x][0]
        else:                       # 출발점으로 가는 경로가 없을 때
            return INF

    if dp[x][visited] != INF:       # 이미 최소비용이 계산되어 있다면
        return dp[x][visited]

    for i in range(1, n):           # 모든 도시를 탐방
        if not graph[x][i]:         # 가는 경로가 없다면 skip
            continue
        if visited & (1 << i):      # 이미 방문한 도시라면 skip
            continue

        # 점화식 부분(위 설명 참고)
        # 아직 아래 식은 <<와 | 때문에 이해 못했는데
        # dp[0][0011] = dp[2][0111] + graph[0][2] 이놈 사례는 이해했다. 0,1,2,3도시가 있으면.
        # 0번도시에서 아직 방문하지 않은 2번, 3번도시를 최적으로 다녀오려면, 
        # 1) 2번도시에서 출발해서 3번을 거쳐서 최종 0번으로 들어가는 경우 + 0번에서 2번 가는 비용
        # 2) 3번도시에서 출발해서 2번을 거쳐서 최종 0번으로 들어가는 경우 + 0번에서 3번 가는 비용
        # 이 두 경우중 min값이 0번도시에서 아직 방문하지 않은 2, 3을 거쳐서 0번으로 되돌아오는 최적의 값임.

        # 스타 2에서 사도가 2번 도시까지는 걸어가고(0번에서 2번 직접 가는 비용) 3번 가는 거는 그림자 분신써서 대신 보내는 상황 그때 걸린 시간 A
        # 사도가 3번 도시까지는 걸어가고(0번에서 3번까지 직접 이동) 2번 가는 거는 그림자 분신 써서 직접 안가고 대신 보낸 상황, 그때 걸린 시간 B
        # min(A,B)해서 최적 선택

        dp[x][visited] = min(dp[x][visited], dfs(i, visited | (1 << i)) + graph[x][i])
    return dp[x][visited]


graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

print(dfs(0, 1))