import sys

input=sys.stdin.readline

A=input().strip().split('-')

for i in range(len(A)):
    temp_nums=0
    if '+' in A[i]:
        temp=A[i].split('+')
        for k in temp:
            temp_nums+=int(k)
            A[i]=temp_nums
    else:
        A[i]=int(A[i])

answer=A[0]
for i in range(1,len(A)):
    answer -=A[i]

print(answer)