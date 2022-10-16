import sys
sys.stdin = open('Week04/1541/1541_lwh.txt', 'r')
input = sys.stdin.readline

data = input().rstrip()

numbers = []
operands = []

num = ''
for x in data:
    if x.isnumeric():
        num += x
    else:
        numbers.append(int(num))
        num = ''
        operands.append(x)

numbers.append(int(num))

try:
    idx_minus = operands.index('-')
    ans = sum(numbers[:idx_minus+1]) - sum(numbers[idx_minus+1:])

except:
    ans = sum(numbers)

print(ans)