from itertools import permutations, combinations

arr = [1,2,3,4,5,6,7,8,9,10]
npr = permutations(arr)
# ncr = combinations(arr,2)

print((len(list(npr))))
# print(list(ncr))

# a = any([0,1,2])
# a = any([0, False, []])