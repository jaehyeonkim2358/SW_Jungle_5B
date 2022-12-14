# https://www.acmicpc.net/problem/1541
# 입력 받는데 숫자와 부호를 나눠서 어케 잘 입력을 받아. (ex A = [55, -, 50, +, 40) >>>어케 받아야할지 모르겠고
# tmp라는 빈 배열을 하나 만들고 tmp에는 최초 괄호 ( 를 하나 넣어놔
# A 배열을 iterating하면서
  # 마이너스가 나오면 )를 tmp에 먼저 넣고 그 다음 마이너스를 tmp에 넣고 바로 ( 도 tmp에 넣어 ex) >>> ") - (" 이런 그림
  # -가 아니면 걍 tmp라는 배열에 넣고 끝
# 이터레이팅이 끝나면 tmp 맨 뒤에 )를 넣어줘
  # tmp는 현재 [ '(', '55', ')', '-', '(', '50', '+', '40', ')' ] 이런 모양임.
# tmp를 int 형식으로 바꿔서 계산을 해줘 >>>이것도 숫자로 계산하기 어케 해야할지 모르겠고
# 무엇보다 이게 왜 그리디인지 모르겟음!


# 복기
import sys
input = sys.stdin.readline

string = input().split('-')
# print(string) #['55', '50+40\n']

sum = 0
for i in string[0].split('+'):
  sum = sum + int(i)

for i in string[1:]:
  for j in i.split("+"):
    sum = sum - int(j)
print(sum)


