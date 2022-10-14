#피보나치 수2

#Fn = Fn-1 + Fn-2 (n ≥ 2)

import sys

n = int(sys.stdin.readline())

fibonacci = []
num = 0

for i in range(n + 1):
    if i == 0:
        num = 0
        
    elif i <= 2:
        num = 1
        
    else:
        num = fibonacci[-1] + fibonacci[-2]

    fibonacci.append(num)
    
    
    
    
print(fibonacci[-1])
