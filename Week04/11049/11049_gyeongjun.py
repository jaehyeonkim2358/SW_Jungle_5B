import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    dp = [[0]*n for _ in range(n)]

    numb = list(map(int, input().split()))
    for _ in range(n-1):
        _, c = map(int, input().split())
        numb.append(c)

    for d in range(n):
        for i in range(n-d):
            j = i + d
            if(i == j):
                continue
            dp[i][j] = 2**31-1
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] +
                        numb[i]*numb[k+1]*numb[j+1])
    print(dp[0][-1])