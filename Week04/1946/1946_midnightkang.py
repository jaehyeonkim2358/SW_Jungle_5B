from sys import stdin

stdin = open("input.txt","r")
input=stdin.readline

t=int(input())

for _ in range(t):
    n=int(input())
    rank=[]
    for _ in range(n):
        rank.append(list(map(int,input().strip().split())))
    rank.sort(key = lambda x : x[0])
    standard=rank[0][1]
    count=1
    for i in range(1,n):     # 면접 기준보다 현 면접 성적이 좋으면 count++ , 기준 갱신 
        tmp=rank[i][1]
        if tmp<=standard:
            count+=1
            standard=tmp
    print(count)
