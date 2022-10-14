# 치우 풀이 참고함!
# 더하기들 먼저 싹 더해놓고 ex) ([50+50], [40+10]이면 [100], [50] 먼저함.)
# 그 다음 100 -50 하는 방식

import sys
input=sys.stdin.readline
A = input().strip().split('-')

# sum = 0 
# 오류 원인: 습관적으로 sum을 전역변수로 써버리면 for문 돌때마다 값이 누적되어버림.

for i in range(len(A)): 
  sum =0 #sum을 여기에 둬서 for문 돌때마가 초기화 해줘야해

  if '+' in A[i]: #문자열이 50+40처럼 +로 이어진 경우
  # 오류 원인: if A[0] in '+': #이렇게 썼네;;
    
    tmp=A[i].split('+')
    for itr_tmp in tmp: 
      sum = sum + int(itr_tmp)
      A[i] = sum

  else: #+로 이어진게 아니라 숫자 하나만 온 경우
    A[i] = int(A[i])

# 정답 출력하는 부분
answer = A[0] #처음 0번째는 무조건 더하기만 되니까 미리 더해놓고
for i in range(1, len(A)):
  answer = answer - A[i]
print(answer)



# 재현이 코드리뷰
# import sys

# A = sys.stdin.readline().rstrip().split('-')

# nums = []
# for a in A:
#     nums.append(sum(map(int, a.split('+'))))  
#이 부분이 진짜 웃겼음. 
#치우처럼 더하기들 먼저 싹 더해놓는 방식이었는데 ex) ([50+50], [40+10]이면 [100], [50] 먼저함.)
#한줄로 구현함.sum(map(int, a.split('+')) 50+50이면 split하면 [50, 50]이지? 이걸 그냥 sum으로 더함.
#끝
"""
치우 코드의 이 부분은 사실 없어도 되는 반복문이었던것.
    tmp=A[i].split('+')
    for itr_tmp in tmp: 
      sum = sum + int(itr_tmp)
      A[i] = sum
"""
# result = nums[0]
# for i in range(1, len(nums)):
#     result -= nums[i]

# sys.stdout.write(f'{result}')