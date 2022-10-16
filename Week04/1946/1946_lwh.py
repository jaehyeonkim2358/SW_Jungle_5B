import sys
sys.stdin = open('Week04/1946/1946_lwh.txt', 'r')
input = sys.stdin.readline

for tc in range(int(input())):
    N = int(input())

    # applicants = [tuple(map(int, input().split())) for _ in range(N)]
    applicants = [None] * 100001
    for i in range(N):
        paper, interview = map(int, input().split())
        applicants[paper] = interview
    
    lowest = applicants[1] 

    cnt = 1

    for applicant in applicants[1:]:
        if applicant == None:
            break
        rank = applicant
        if rank < lowest:
            lowest = rank
            cnt += 1
    
    print(cnt)