import math
import sys
sys.stdin = open("W03-W04/Week04/2253/input.txt","r")

n, m = map(int, input().split())
INF = n     # lesson 최대값을 무조건 float('inf')로 안해도 된다.
limit = lambda x : int((-1+ math.sqrt(1+8*x))/2)

dp = [[INF]*(limit(n)+1) for _ in range(n+1)]
dp[2][1] = 1

cant = {int(sys.stdin.readline()) for _ in range(m)}

def go(n, dp, cant, limit):
    if 2 in cant :
        return -1
    
    for rock in range(3,n+1):
        if rock in cant:
            continue
        
        for step in range(1, limit(rock)+1): # 각 스텝 순회
            prev_rock = dp[rock-step]
            tmp = INF
            for i in range(step-1, step+2):     # (step-1, step, step+1)
                if i < 1 or limit(rock) < i:
                    continue
                if prev_rock[i] + 1 < tmp:
                    tmp =  prev_rock[i] + 1
            dp[rock][step] = tmp
    
    return min(dp[n])

print(go(n,dp,cant,limit))      # 2번 돌이 열려있다면 마지막 돌까지 어떻게든 갈수는 있다. 따라서 못가는 경우는 2번 돌이 막혀있는 경우 밖에 없다.