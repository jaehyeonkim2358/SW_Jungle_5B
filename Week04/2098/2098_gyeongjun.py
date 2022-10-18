import sys
input = sys.stdin.readline

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dp = [[-1 for _ in range(1 << n)] for _ in range(n)]
inf = 9876543210

def recursion(cur, visited):
    # all node visit
    if visited == (1 << n)-1:
        if board[cur][0] == 0:
            return inf
        dp[cur][visited] = board[cur][0]
        return board[cur][0]

    # memoization
    if dp[cur][visited] != -1:
        return dp[cur][visited]

    min_dist = inf
    for i in range(n):
        # if not visited i-node yet + board not zero
        if not visited & (1 << i) and board[cur][i] != 0:
            min_dist = min(min_dist, board[cur][i] + recursion(i, visited | (1 << i)))

    dp[cur][visited] = min_dist
    return min_dist

print(recursion(0, 1))
print(dp)