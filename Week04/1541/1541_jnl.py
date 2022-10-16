# 잃어버린 괄호
import sys
input = sys.stdin.readline
print = sys.stdout.write

formula = input().rstrip()

def solution():
    subTotal = [0] 
    tmp = ''
    for char in formula:
        if char in '+-':
            if char == '+':
                subTotal[-1] += int(tmp)
            else:
                subTotal[-1] += int(tmp)
                subTotal.append(0)
            tmp = ''
        else:
            tmp += char
    subTotal[-1] += int(tmp)

    result = 0
    for idx, sub in enumerate(subTotal):
        if idx == 0:
            result = sub
        else:
            result -= sub
    return result
print(f'{solution()}')
    

