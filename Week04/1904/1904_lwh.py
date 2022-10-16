import sys
sys.stdin = open('Week04/1904/1904_lwh.txt', 'r')
input = sys.stdin.readline

# tile = [0] * 1000001

N = int(input())
# tile[1] = 1
# tile[2] = 2
tile = [2, 1]

def solve(n):
    
    for m in range(3, n+1):
        tile[m%2] = (tile[0] % 15746 + tile[1] % 15746) % 15746
    
    return tile[n] 

print(solve(N))