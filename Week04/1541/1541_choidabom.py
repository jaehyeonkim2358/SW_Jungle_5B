# 1541: 잃어버린 괄호
import sys
sys.stdin = open("1541/input.txt","r")

# 괄호를 다 치는 경우의 수를 생각했는데
# 최소값은 -를 기준으로 괄호를 넣으면 최소값이 됨
# ex) 55-50+40 
# 1) 55-(50+40) = -35 / 2) (55-50)+40 = 45 / 3) (55-50+40) = 45  
oper = sys.stdin.readline().rstrip().split('-') # sso, -를 기준으로 문자열을 나눠준다. 

# print(oper) ['55', '50+40']
for i in range(len(oper)):
    nums = 0
    if '+' in oper[i]: # 수식 안에 '+'가 있으면 
        tmp = oper[i].split('+') # ['50', '40']
        for j in tmp:
            nums += int(j)
            oper[i] = nums
    else:
        oper[i] = int(oper[i])

answer = oper[0] # 식의 첫 친구는 빼면 안 됨
for i in range(1, len(oper)): # 그래서 for문을 1부터 oper의 길이만큼 ~
    answer -= oper[i]         # 빼는 일만 남았다 ~!ㄴ

print(answer)