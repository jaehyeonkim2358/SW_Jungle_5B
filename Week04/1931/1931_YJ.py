import sys
sys.stdin = open( "input.txt", "r" )
input = sys.stdin.readline

N = int(input())
meetings= []
for i in range(N):
    start, end = map(int, input().split())
    meetings.append((end,start)) # lambda 쓰지 않고 하려고 그냥 end를 먼저 넣었음 

meetings.sort()
finishing_time= 0 
meeting_num= 0 #미팅의 수 
for meeting in meetings:
    #시작 시간이 끝나는 시간보다 같거나 크면 미팅을 넣고, meeting_num+=1
    if meeting[1] >= finishing_time :
        meeting_num +=1
        finishing_time= meeting[0]
print(meeting_num)
