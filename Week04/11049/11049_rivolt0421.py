import sys
sys.stdin = open("W03-W04/Week04/11049/input.txt","r")
rl = sys.stdin.readline

n = int(input())
C = [[float('inf')] * (n) for _ in range(n)]
d = list(map(int, rl().split()))            # 행렬 속성 정보 (r*c) 저장.
for i in range(n-1):
        d.append(int(rl().split()[1]))

# C 초기화
for i in range(n):
    C[i][i] = 0
    
def go(n, C, d):
    for L in range(1, n):           # L = 부분 문제의 크기를 조절하는 인덱스 (이 코드에서는 부분 문제 안의 곱셈의 개수.)
        for i in range(0, n-L):     # i = 부분 문제 시작 행렬 인덱스
            j = i + L               # j = 부분 문제 끝   행렬 인덱스

            for k in range(i, j):
                tmp = C[i][k] + C[k+1][j] + (d[i]*d[k+1]*d[j+1])
#                       21째 줄에서 더해지는 각 요소들.              
#
# (A_i * A_(i+1) * ... * A_k)         *         (A_(k+1) * A_(k+2) * ... * A_j)
# ---------------------------        ---        -------------------------------
#              ⬇                      ⬇                       ⬇
#          C[i][k]           d[i]*d[k+1]*d[j+1]           C[k+1][j]
#                                             
                if C[i][j] > tmp:
                    C[i][j] = tmp
            
    return C[0][n-1]

print(go(n, C, d))

# dp 테이블 미리 공간 만들어 놓지 않고, 하나씩 append하며 진행하는 방식.
# 효율성에 차이가 없다.
# n = int(input())
# C = [[0] for _ in range(n)]
# d = []
# for i in range(n):
#     if i != 0:
#         d.append(int(rl().split()[1]))
#     else:
#         d += list(map(int, rl().split()))

# def go(n, C, d):
#     for L in range(1, n):
#         for i in range(0, n-L):
#             j = i + L
#             min_ = float('inf')
#             for k in range(i, j):
#                 tmp = C[i][k-i] + C[k+1][j-(k+1)] + (d[i]*d[k+1]*d[j+1])
#                 if min_ > tmp:
#                     min_ = tmp
#             C[i].append(min_)
#     return C[0][n-1]

# print(go(n, C, d))