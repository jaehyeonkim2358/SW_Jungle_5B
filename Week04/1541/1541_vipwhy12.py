import imp


import sys
from unittest import result

lose_parenthesis = sys.stdin.readline().rstrip().split('-')

nums = []

for parenthesis in lose_parenthesis:
    nums.append(sum(map(int, parenthesis.split('+'))))

result = nums[0]

for i in range(1, len(nums)):
    result -= nums[i]
    
print(result)