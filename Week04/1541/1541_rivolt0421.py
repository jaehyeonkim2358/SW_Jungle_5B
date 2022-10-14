from functools import reduce
import sys
sys.stdin = open("W03-W04/Week04/1541/input.txt","r")

line = sys.stdin.readline().strip()

for_minus = []
for chunk in line.split('-'):
    for_plus = []
    for num in chunk.split('+'):
        for_plus.append(int(num))
    for_minus.append(reduce(lambda x,y: x+y, for_plus))

print(reduce(lambda x,y: x-y, for_minus))