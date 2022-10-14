## DP memoization 방식과 상향식 방법 모두 python3 기준 30840kb 68ms 로 메모리/시간 동일 

N = int(input())

def fib(n) :
    if n == 0 or n==1 :
        return n
    a, b = 0, 1 # 초깃값 두 수 
    for i in range (1, N) :
        temp= a
        a = b
        b= temp+a
    return b

print(fib(N))

