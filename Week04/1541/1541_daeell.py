import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

m = input().split('-')

list = []
for i in m:
    numbers = i.split('+')
    tmp = 0
    for i in range(len(numbers)):
        tmp += int(numbers[i])
    list.append(tmp)

for i in range(1, len(list)):
    list[0] -= list[i]

print(list[0])
