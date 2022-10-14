ans = [0,1]
def Leonardo_Fibonacci(n):
    if n<len(ans):
        return ans[n]
    ans.append(Leonardo_Fibonacci(n-1)+Leonardo_Fibonacci(n-2))
    return ans[n]
n = int(input())
print(Leonardo_Fibonacci(n))