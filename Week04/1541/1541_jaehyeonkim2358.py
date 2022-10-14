import sys

A = sys.stdin.readline().rstrip().split('-')

nums = []
for a in A:
    nums.append(sum(map(int, a.split('+'))))

result = nums[0]
for i in range(1, len(nums)):
    result -= nums[i]

sys.stdout.write(f'{result}')
