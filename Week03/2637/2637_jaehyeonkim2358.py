# https://dapsu-startup.tistory.com/entry/백준-장난감-조립-2637-파이썬Python

import sys
from collections import defaultdict, deque

def main():
    # 입력 및 변수 선언
    N = int(sys.stdin.readline().rstrip())
    M = int(sys.stdin.readline().rstrip())

    graph = defaultdict(set)
    in_degree = [0] * (N+1)     # 진입 차수
    used = [[0] * (N+1) for _ in range(N+1)]    # 사용 갯수를 누적해서 계산하기 위한 2차원 리스트
    start = []

    # 그래프, 진입차수, 최초 진입차수가 0인 정점을 입력값에 따라 저장
    set_value(N, M, graph, in_degree, start)

    # 위상 정렬을 이용한 가중치 연산 결과를 used[][]에 저장
    solution(start, graph, used, in_degree)

    # 기본 부품(최초 진입차수가 0인 정점)이 완제품(최초 진출 차수가 0인 정점)에 사용된 갯수를 출력
    for s in start:
        sys.stdout.write(f'{s} {used[N][s]}\n')

# 입력
def set_value(N, M, graph, in_degree, start):
    for _ in range(M):
        x, y, k = map(int, sys.stdin.readline().split())
        graph[y].add((x, k))
        in_degree[x] += 1
    
    for i in range(1, N+1):
        if in_degree[i] == 0:
            start.append(i)
    

def solution(root, graph, used, in_degree):
    queue = deque(root)

    while queue:
        cur = queue.popleft()
        # print_used(used)
        for next, needs in graph[cur]:
            # 인접 정점의 진입 차수 감소
            in_degree[next] -= 1

            # 다음 정점의 진입 차수가 0이되면 queue에 넣어준다.
            if in_degree[next] == 0:
                queue.append(next)

            # 현재 정점의 최초 진입 차수가 0이었다면,
            if cur in root:
                # 가중치를 더해줌
                used[next][cur] += needs
            # 그 외의 경우
            else:
                # 현재 정점에서 다음 정점으로의 가중치와 현재 정점에 지금까지 누적된 가중치 합을 곱해줌
                for i in range(1, len(used[next])):
                    used[next][i] += used[cur][i] * needs



# def print_used(used):
#     for i in range(len(used)):
#         print(*used[i], sep=" ")
#     print("================")
            


if __name__ == '__main__':
    main()
