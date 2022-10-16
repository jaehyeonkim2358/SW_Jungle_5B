import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    applicants = [None] * (n+1)
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        applicants[a] = b

    rank = n+1
    count = 0
    for i in range(1, n+1):
        if applicants[i] < rank:
            rank = applicants[i]
            count += 1
            
    sys.stdout.write(f'{count}\n')