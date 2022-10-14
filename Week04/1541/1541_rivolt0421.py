from functools import reduce        # lesson 이 import가 시간을 좀 소비한다. 40ms 차이가 났다.
import sys
sys.stdin = open("W03-W04/Week04/1541/input.txt","r")

# 반복문 사용 30840kb 68ms
line = sys.stdin.readline().strip()

for_minus = []
for chunk in line.split('-'):
    for_minus.append(sum(map(int,chunk.split('+'))))
    
result = for_minus[0]
for num in for_minus[1:]:
    result -= num
print(result)

# reduce 사용 32392kb 100ms
# for_minus = []
# for chunk in line.split('-'):
#     for_plus = []
#     for num in chunk.split('+'):
#         for_plus.append(int(num))
#     for_minus.append(reduce(lambda x,y: x+y, for_plus))

# print(reduce(lambda x,y: x-y, for_minus))