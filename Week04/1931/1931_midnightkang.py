from sys import stdin

stdin = open("input.txt","r")
input=stdin.readline

n=int(input())
# 이 문제의 그리디 = 가장 빨리 끝나는 강의  (이게 제일 탐욕적이다 ) (이 방법이 모순이 없다 ) (남은 자원을 최대로 활용한다)


schedule=[]
for _ in range(n):
    schedule.append(list(map(int,input().strip().split())))
schedule.sort(key=lambda x:x[0])  # 종료시간이 같을 경우 추후에 중복 카운트 방지 
schedule.sort(key=lambda x:x[1])


k=0
count=0

for start,end in schedule:
    if start>=k:
        count+=1
        k=end
        

        
print(count)
