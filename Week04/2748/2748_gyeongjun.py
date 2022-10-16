import sys
input = sys.stdin.readline

a = int(input())

fibo_arr = [0,1]
#피사노 주기: 피보나치 수를 K로 나눈 나머지는 항상 주기를 갖게된다
for i in range(2,a+1):
    fibo_arr.append(fibo_arr[i-1]+fibo_arr[i-2])
print(fibo_arr[a])