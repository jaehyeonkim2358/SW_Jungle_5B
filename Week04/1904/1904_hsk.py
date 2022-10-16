import sys
sys.stdin = open("input.txt","r")
# 02. https://www.acmicpc.net/problem/1904 : 01타일

# 2진 수열 0 또는 1
# 0 두개를 00으로 붙힘 >> 00 또는 1로 된 타일
# 지원이가 만들수 있는 가짓수 
# 만들수 있는 개수를 15746 으로 나누 나머지
# 

n = int(input())

dp = [0] * (n+1)
for i in range(1, n+1):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 2
    else:
        a = (dp[i-1] + dp[i-2])
        dp[i] = a%15746
print(dp[-1])