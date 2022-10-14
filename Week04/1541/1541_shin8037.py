import sys

input=sys.stdin.readline

A=input().strip().split('-') # 최소값은 -를 기준으로 괄호를 넣으면 최소값이 됨

for i in range(len(A)):
    temp_nums=0
    if '+' in A[i]: # 원소가 +를 가지고 있으면 합쳐줌
        temp=A[i].split('+')
        for k in temp:
            temp_nums+=int(k)
            A[i]=temp_nums
    else:
        A[i]=int(A[i]) # 없으면 그냥 정수형으로 전환

answer=A[0] # 처음에는 무조건 + 
for i in range(1,len(A)): # 그외에는 다 빼주면 됨
    answer -=A[i]

print(answer)