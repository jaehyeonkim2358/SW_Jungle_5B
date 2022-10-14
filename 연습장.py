import sys

input=sys.stdin.readline
A = input().strip().split('-')
sum = 0
for i in range(len(A)): #입력받은 문자열에서 -를 기준으로 나눴고 ex(50+40 - 55) 처음 50+40을 뺀 나머지는 -(55)처럼 전부 마이너스 붙여주면 최솟값 나온다.

  if '+' in A[i]: #문자열이 50+40처럼 +로 이어진 경우
  # if A[0] in '+': #이렇게 썼네;;(충분히 다시 할 수 있는 버릇)
    
    tmp=A[i].split('+')
    for itr_tmp in tmp: #50
      sum = sum + int(itr_tmp)
      A[i] = sum
  else: #+로 이어진게 아니라 숫자 하나만 온 경우
    A[i] = int(A[i])

answer = A[0] #처음 0번째는 무조건 더하기만 되니까 미리 더해놓고
for i in range(1, len(A)):
  answer = answer - A[i]
print(answer)