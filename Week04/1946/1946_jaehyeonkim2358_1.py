import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    applicants = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(n)], key=lambda x: x[0])

    rank = n+1
    count = 0
    for a in applicants:
        if a[1] < rank:
            rank = a[1]
            count += 1
    sys.stdout.write(f'{count}\n')