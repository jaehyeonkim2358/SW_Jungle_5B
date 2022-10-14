import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/week04_Baekjoon/SW_Jungle_5B/input.txt","r")

t = int(input())
for _ in range(t) :
    n = int(input())
    money = list(map(int, sys.stdin.readline().strip().split()))
    m = int(input())

    dp = [0] * (m + 1)
    dp[0] = 1
    
    for mn in money :   # 가능한 화폐 조합
        for i in range(1, m+1) : # 1원부터 m원까지
            if i >= mn :
                dp[i] += dp[i-mn]
    print(dp[m])
