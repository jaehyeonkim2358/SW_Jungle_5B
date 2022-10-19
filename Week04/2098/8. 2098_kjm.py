# https://www.acmicpc.net/problem/2098
import sys
input = sys.stdin.readline
n=int(input())

INF = sys.maxsize
# dp = [[INF] * (1<<n) for _ in range(n)] #내기준으론..괜히 10진법으로 표현하면 될걸 2진법으로 꼬아서 표현한 느낌인 코드임..
dp = [[INF] * (2**n) for _ in range(n)] #도시 1를 방문했냐 안했냐를 체킹할거라(도시당 경우의 수 2임)

graph=[]
for i in range(n):
    graph.append(list(map(int, input().split())))
# print(graph) [[0, 10, 15, 20], [5, 0, 9, 10], [6, 13, 0, 12], [8, 8, 9, 0]]

def dfs(x, visited): #여기서 x는 출발 도시가 아니라 현재도시라는 점을 기억해야해!! 출발도시는 항상 0번 도시로 고정해놓은 상태야.
    if visited == (1<<2)-1: #2진법으로 15이면 111,111,111,111,111 이다. 즉 1이 도시를 방문한거고 0이 도시를 방문 안 한거라 생각하면 15는 15개의 도시(시작도시 1을 뺀)를 모두 방문한 것을 표현한 것이다.
        if graph[x][0]: #출발점으로 되돌아가는 경로가 있을 때
            return graph[x][0] #그 경로의 비용을 리턴해라??
        else: #출발점으로 되돌아가는 경우가 없으면 
            return INF
    if dp[x][visited] != INF: #초깃값을 무한대로 줬잖아? 근데 어떤 도시를 방문했는데 INF가 아니다? 이미 최솟값으로 갱신해놓은 곳이다.
        return dp[x][visited] #그냥 dp[x][visited]값을 리턴하면 됨.
    
    for i in range(1,n): #예외처리 했고 이제야 모든 도시를 탐방해보자
        path= graph[x][i]
        if path==0: #가는 경로가 없다면 skip #not 10: 이게 뭔소린가 싶은데 그냥 0만 아니면 
            continue
        if visited & (1<<i): #이미 방문한 도시라면 skip
            continue

        dp[x][visited] = min(dp[x][visited]), dfs(i, visited | (1<<i)+graph[x][i]) #visited | (1<<i) 이게 비트마스킹을 최신화 시키고있네? 
    return dp[x][visited]

print(dfs(0,1))
