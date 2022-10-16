import sys
sys.stdin = open("input.txt", "r")
input= sys.stdin.readline

T = int(input())
def do_the_cases(T):
    for i in range(T):
        N= int(input())
        ranks = [None for _ in range(N+1)]
        cnt = 0 # 합격자 수 
        for i in range(N):
            document, interview = map(int, input().split())
            ranks[document] = interview
        lowest_interview_rank = N+1
        for i in range(1, N+1) :
            if ranks[i] < lowest_interview_rank : #면접 등수가 최저 면접 등수보다 작을 때 (즉 등수가 더 높을 때)
                cnt +=1 # 합격자!
                lowest_interview_rank = ranks[i]
        print(cnt) 
do_the_cases(T)
