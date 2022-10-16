# LCS
import sys
input = sys.stdin.readline
print = sys.stdout.write
A = ' '+ input().rstrip()
B = ' '+ input().rstrip()

LCS = [[0]*(len(B)+1) for _ in range(len(A)+1)]
for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j] :
            LCS[i][j] = LCS[i-1][j-1]+1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

print(f'{LCS[len(A)-1][len(B)-1]}')