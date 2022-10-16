import sys
sys.stdin = open("input.txt","r")
# 04. https://www.acmicpc.net/problem/9251: LCS
input = sys.stdin.readline

a_arr = ["0"] + list(map(str, list(input().rstrip())))
b_arr = ['0'] + list(map(str, list(input().rstrip())))

lcs = [[0] * (len(b_arr)) for _ in range(len(a_arr))]

# Longest Common Substring
# for i in range(len(a_arr)):
#     for j in range(len(a_arr)):
#         if i == 0 or j == 0:
#             lcs[i][j] = 0
#         elif a_arr[i] == b_arr[j]:
#             lcs[i][j] = lcs[i-1][j-1] + 1
#         else:
#             lcs[i][j] = 0
# print(lcs)

# Longest Common Subsequence

for i in range(1, len(a_arr)):
    for j in range(1, len(b_arr)):
        if a_arr[i] == b_arr[j]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
print(lcs[-1][-1])