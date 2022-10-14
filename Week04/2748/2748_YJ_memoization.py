## DP memoization 방식과 상향식 방법 모두 python3 기준 30840kb 68ms 로 메모리/시간 동일 

N = int(input())

def fib(n, memo={}) :
    if n == 0 or n==1 :
        return n
    if not memo.get(n) : # memo 에 n 값이 없으면 
        memo[n] = fib(n-2) + fib(n-1) #재귀 후 해시테이블에 저장
    return memo[n]

print(fib(N))

