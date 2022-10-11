import sys
from collections import defaultdict
from collections import deque
sys.stdin = open('2606/2606_lwh.txt', 'r')
input = sys.stdin.readline

def bfs(v, infected, computers):
    queue = deque()
    queue.append(v)
    infected[v] = True
    while queue:
        v = queue.popleft()
        for friend in computers[v]:
            if not infected[friend]:
                infected[friend] = True
                queue.append(friend)
    print(infected.count(True)-1)

def init():
    N = int(input())
    M = int(input())
    computers = defaultdict(list)
    infected = [False] * (N+1)
    for _ in range(M):
        edge = list(map(int, input().split()))
        v, u = edge[0], edge[1]
        computers[u].append(v)
        computers[v].append(u)
    
    bfs(1, infected, computers)

init()

