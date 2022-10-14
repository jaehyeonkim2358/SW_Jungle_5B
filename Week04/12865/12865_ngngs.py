import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/week04_Baekjoon/SW_Jungle_5B/input.txt","r")

# 냅색 알고리즘(표참고) https://claude-u.tistory.com/208
# 냅색 알고리즘(설명참고) https://hongcoding.tistory.com/50

n, k = map(int, sys.stdin.readline().strip().split())
stuff = [[0, 0]]
graph = [[0 for _ in range(k+1)] for _ in range(n+1)]
# print(graph)

for _ in range(n) :
    stuff.append(list(map(int, sys.stdin.readline().strip().split())))
# print(stuff)

for i in range(1, n+1) :
    for j in range(1, k+1) :
        weight = stuff[i][0]
        value = stuff[i][1]

        if j < weight : # 넣을 게 무과 초과라면.
            graph[i][j] = graph[i-1][j] # 바로 한 칸 위
        else :
            graph[i][j] = max(graph[i-1][j], value + graph[i-1][j-weight]) 
            # 한 칸 위 vs 넣을물건의 value + (최대한도 - 넣을물건의 무게)의 value 

print(graph[n][k])