import sys
sys.stdin = open("input.txt","r")
# 06. https://www.acmicpc.net/problem/11049 : 행렬 곱셈 순서
input = sys.stdin.readline

# 크기가 n*m 행렬 a 
n = 5
m = 3
k = 2
s = 6
print((n*m*k)+(n*k*s))
print((n*m*s)+(m*k*s))