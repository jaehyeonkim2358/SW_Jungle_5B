import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/week04_Baekjoon/SW_Jungle_5B/input.txt","r")

calc = sys.stdin.readline().strip().split('-')  # '-'가 등장했을 때 뒤에 값이 최댓값이 되어야함.
# print(calc) # ['55', '50+40']

ans = []

for num in calc :
    cnt = 0
    calc2 = num.split('+')
    for num2 in calc2 :
        cnt += int(num2)
    ans.append(cnt) 
    
n = ans[0]  # idx가 0값인 이후로는 다 뺄셈을 할거기 때문에.
for i in range(1, len(ans)) :
    n -= ans[i] 
# print(n)