import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
plus, minus, multi, div = map(int, input().split())

maxN = -sys.maxsize
minN = sys.maxsize


def dfs(num, idx, plus, minus, mul, div):
    global maxN, minN
    if idx == N:
        maxN = max(num, maxN)
        minN = min(num, minN)
        return
    if plus:
        dfs(num+nums[idx], idx+1, plus-1, minus, mul, div)
    if minus:
        dfs(num-nums[idx], idx+1, plus, minus-1, mul, div)
    if mul:
        dfs(num*nums[idx], idx+1, plus, minus, mul-1, div)
    if div:
        dfs(int(num/nums[idx]), idx+1, plus, minus, mul, div-1)


dfs(nums[0], 1, plus, minus, multi, div)

print(maxN)
print(minN)
