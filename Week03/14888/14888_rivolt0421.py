import sys
sys.stdin = open("W03-W04/Week03/14888/input.txt","r")

n = int(input())
l = list(map(int, input().split()))
p, mi, mul, d = map(int, input().split())
Mm =[-float('inf'),float('inf')]
#   [     Max     ,     min    ]

def go(l, p, mi, mul, d, result, i, Mm):
    if p:
        go(l, p-1, mi, mul, d, result+l[i], i+1, Mm)
    if mi:
        go(l, p, mi-1, mul, d, result-l[i], i+1, Mm)
    if mul:
        go(l, p, mi, mul-1, d, result*l[i], i+1, Mm)
    if d:
        if result ^ l[i] < 0 : result = -1*(abs(result)//abs(l[i]))
        else : result //= l[i]
        go(l, p, mi, mul, d-1, result, i+1, Mm)
    
    if i == len(l):
        Mm[0] = max(Mm[0],result)
        Mm[1] = min(Mm[1],result)
        
go(l, p,mi,mul,d, l[0],1, Mm)
print(*Mm, sep='\n')

# ops = ['+']*p + ['-']*mi + ['*']*mul + ['//']*d
# visited = [0] * (n-1)
    
# def go2(l, result, ops, i, visited, Mm, depth):
#     visited[i] = 1
    
#     if ops[i] == "//" and result ^ l[depth+1] < 0:
#         result = -1 * (abs(result)//abs(l[depth+1]))
#     else:
#         result = eval(f'result{ops[i]}{l[depth+1]}')
    
#     if depth == (n-2):
#         Mm[0] = max(Mm[0],result)
#         Mm[1] = min(Mm[1],result)
#         return
    
#     for i in range(n-1):
#         if not visited[i]:
#             go2(l, result, ops, i, visited, Mm, depth+1)
#             visited[i] = 0   

# for i in range(n-1):
#     go2(l, l[0], ops, i, visited, Mm, 0)
#     visited[i] = 0
    
# print(*Mm, sep='\n')