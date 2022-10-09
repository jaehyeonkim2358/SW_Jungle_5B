# 풀이 참고
# https://kth990303.tistory.com/141

import sys
sys.setrecursionlimit(10**9)

def dfs(start: int) -> int:
    count = 0
    for next in path[start]:
        if A[next] == '1':
            count += 1
        else:
            if visited[next] is False:
                visited[next] = True
                count += dfs(next)
    return count


n = int(sys.stdin.readline().rstrip())          # 전체 정점의 수
A = ' '+sys.stdin.readline().rstrip()           # 정점의 실내/실외 정보를 담은 문자열. index와 정점번호를 맞춰주기 위해 공백 한 칸(' ')을 앞에 붙여줌
path = [[] for _ in range(n+1)]                 # 인접 리스트 형태로 경로를 입력 받음
visited = [False] * (n+1)                       # 방문 여부를 확인하기 위한 bool type 배열
answer = 0                                      # 가능한 서로 다른 산책 경로의 수(정답)

# n개의 정점을 n-1개의 간선으로 이어줌
for _ in range(n-1):
    u, v = map(int ,sys.stdin.readline().split())
    # 방향이 존재하지 않기 때문에 입력된 간선의 두 정점 인접 리스트에 서로를 넣어줌
    path[u].append(v)
    path[v].append(u)


# 전체 정정을 순회
for i in range(1, n+1):
    # 현재 정점이 실내일 경우
    if A[i] == '1':
        # 실내 정점과 인접한 실내 정점 수 만큼 경로 수 증가
        for j in path[i]:
            if A[j] == '1':
                answer += 1
    # 현재 정점이 실외인 경우
    else:
        # 방문하지 않은 실외일 때
        if visited[i] is False:
            visited[i] = True       # 방문체크
            count = dfs(i)          # 현재 실외 정점에서 도달 가능한 실내 정점의 개수
            # '현재 실외 정점에 연결된 실내 정점간 연결 가능한 경우의 수 (n*(n-1))'가
            # 현재 실외 정점을 포함한 '서로 다른 산책 경로의 수' 이므로, 계산 후 가능한 전체 경로의 수에 더해줌
            answer += count * (count-1)

print(answer)