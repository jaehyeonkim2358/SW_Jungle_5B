import sys
sys.stdin = open('Week04/1904/1904_lwh.txt', 'r')
input = sys.stdin.readline

tile = [0] * 1000001

N = int(input())
tile[1] = 1
tile[2] = 2

def solve(n):
    if n <= 2:
        return tile[n]
    
    for m in range(3, n+1):
        tile[m] = (tile[m-1]%15746 + tile[m-2]%15746)%15746
    
    return tile[n] 

print(solve(N))