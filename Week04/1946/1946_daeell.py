# 44600 3204
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def get_success():
    n = int(input())
    _list = [tuple(map(int, input().split())) for _ in range(n)]
    _list.sort()
    # 일단 서류 심사 순으로 정렬
    ans = 1
    # 일단 서류 심사 1등은 무조건 한 과목은 누구보다 높다는 의미이므로 탈락 조건이 아님.
    tmp = _list[0]
    for i in range(1, n):
        if _list[i][1] < tmp[1]:
            # 필기성적의 등수가 비교대상 지원자보다 더 높다면 (등수가 적다면) 합격
            tmp = _list[i]
            ans += 1
    print(ans)


t = int(input())

for _ in range(t):
    get_success()

# 시간초과 (반복문으로 확인)
# t = int(input())

# for _ in range(t):
#     applicant_num = int(input())
#     applicants = [tuple(map(int, input().split()))
#                   for _ in range(applicant_num)]
#     ans = 0
#     for i in range(applicant_num):
#         for j in range(applicant_num):
#             flag = True
#             if i == j:
#                 continue
#             elif applicants[i][0] > applicants[j][0] and applicants[i][1] > applicants[j][1]:
#                 flag = False
#                 break
#         if flag == False:
#             continue
#         else:
#             ans += 1
#     print(ans)
