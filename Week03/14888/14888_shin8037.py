import sys
sys.setrecursionlimit(10**8)

input=sys.stdin.readline

N=int(input())

A=(list(map(int,input().strip().split())))

command=(list(map(int,input().strip().split())))

print(command)

sum=0
answer_max=-9999999999
answer_min=9999999999

def dfs(cnt,sum):
    global answer_max,answer_min, N

    if cnt==N:
        answer_max=max(answer_max, sum)
        answer_min=min(answer_min, sum)
        return
        
    for i in range(4):
        if command[i]>0:
            command[i] -=1 # 해당 커맨드를 사용하면 -1 로 해주고

            if i==0:                
                dfs(cnt+1,sum+A[cnt])
            elif i==1:                
                dfs(cnt+1,sum-A[cnt])
            elif i==2:                
                dfs(cnt+1,sum*A[cnt])
            elif i==3:                
                if sum>=0:
                    dfs(cnt+1,sum//A[cnt])
                else:
                    dfs(cnt+1,(sum*-1)//A[cnt]*(-1))

            command[i] +=1 # 해당 커맨드 사용후 다시 채워넣기 안그러면 한번만 돌고 끝나버림 --> 앞 방향에서 한번 돌았으면 역순으로도 돌게하고 넣었다 빼줬다 하면서 여러가지 경우의 수를 돌수 있게 해줌


dfs(1,A[0])
print(answer_max)
print(answer_min)
