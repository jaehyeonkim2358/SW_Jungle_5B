import sys
sys.stdin = open("W03-W04/Week04/11047/input.txt","r")

n, k = map(int, sys.stdin.readline().split())

l = []
for _ in range(n):
    x = int(sys.stdin.readline().strip())
    if x > k:
        break
    l.append(x)

ans = 0
for i in range(1, len(l)+1):
    coin = l[-i]
    if k < coin :   # 동전 가치가 더 크면 넘어가야 함.
        continue
    
    x = k / coin
    
    ans += int(x)   # 동전 개수 추가.
    k %= coin       # 가치 갱신
    
    if x % 1 == 0:  # 딱 맞아 떨어졌으면 그만.
       break
   
print(ans)
    
    
    