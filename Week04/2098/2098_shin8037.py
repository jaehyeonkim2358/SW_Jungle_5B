import sys
input=sys.stdin.readline

n=int(input().strip())

A=[]
for i in range(n):
    A.append(list(map(int,input().strip().split())))


dp=list([0]*(1<<n-1)for _ in range(n))

def tsp(now, route):
    if dp[now][route] != 0: # 0 이 아니라면 == 현재 온 곳의 route가 이미 기록되어있는 경로라면
        return dp[now][route] # 저장된 값을 리턴 - dp: memoization
    if route==(1<<n-1)-1: # 모든 경로를 순회했다면 (비트마스킹 - (111))
        if A[now][0]: # 그리고 현재위치에서 출발지로 가는 길이 있다면
            return A[now][0] # 현재에서 출발지로 가는 비용을 return
        return sys.maxsize # 출발지로 못가면 실패한 경로이니깐 max로 채워줌
    
    answer=sys.maxsize # 일단 최대비용으로 시작 경로를 순회할때마다 나오는 최소값을 넣어줄 예정
    for next in range(1,n): # 1번 도시 부터 돈다 -- 어차피 시작점이 어디든 같은 값을 가짐 따라서 0번에서 시작했다고 가정
        if A[now][next]==0: # 현재 도시에서 다음 도시로 가는 길이 없으면
            continue # 무시하고 다음 도시로
        if route & 1<<(next -1): # 현재 지나온 경로 == route, (1<<next-1) ==지금 지나는 경로 둘이 true이면 이미 지나온 경로라는 뜻
            continue # 무시하고 다음 도시로

        cost=A[now][next]+tsp(next,route|(1<<next-1)) 
        
        #비용 = 현재도시에서 다음도시 가는 비용 + tsp(다음 도시, route == 지금까지 지나온 경로, (1<<next-1) == 현재 지나고 있는 경로)

        # -> 다음도시까지의 비용 + tsp(다음도시, route에 다음 도시 포함시키기 (지나온 경로로 만들기))
        if answer>cost: # 여기에서 최소 비용을 걸러내게된다
            answer=cost
    
    dp[now][route]=answer
    #재귀가 끝나면 모든 순회를 다 돌고나서 최소 값이 dp[0][0] 에 저장될 것 - 처음 시작이 0이었고 돌아온곳도 0이어야하니깐
    
    return answer # 혹은 return dp[0][0]

print(tsp(0,0))


