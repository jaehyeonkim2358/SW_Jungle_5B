import sys
sys.stdin = open("input.txt","r")
# 11. https://www.acmicpc.net/problem/1541: 잃어버린 괄호
input = sys.stdin.readline

# 가만 생각해 보니 괄호를 꼭 넣어야 하나

a = input().split('-') # 문자열에서 '-'를 빼고 받음

arr = []
for i in a:
    arr.append(i.split('+')) # '+'를 기준으로 같은 리스트에 묶음

arr_m = []
for i in arr:
    arr_m.append(list(map(int, i))) # 정수형으로 형변환

result = 0
for i in range(len(arr_m)): 
    if i == 0: # 첫번째는 무조건 더해서 넣어줌
        result = sum(arr_m[i])
    else: # 뒤 리스트는 더한 후 앞 리스트의 수들과 '-'
        result -= sum(arr_m[i])

print(result)

        



