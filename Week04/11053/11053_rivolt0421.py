import sys
sys.stdin = open("W03-W04/Week04/11053/input.txt","r")
# LIS (Longest Increasing Subsequence)

# # 1. O(n^2)
# # dp[i] 는 l[i]를 마지막 원소로 가지는 증가하는 부분 수열의 최대 길이
# # 원본 수열의 각 원소는 스스로를 하나의 원소로 가지는 부분수열이 될 수 있으므로, dp의 모든 값을 1로 초기화 해준다.
# n = int(input())
# dp = [1] * n
# l = list(map(int, sys.stdin.readline().split()))

# # 부분 수열 안에서 원소들이 증가하는 순서를 가져야 하는 것은 맞는데,
# # 부분 수열 원소들이 원래 수열에서의 가졌던 순서 또한 지켜져야 한다.
 
# for i in range(1,n):    # 그래서 이렇게 원래 수열에서 원소를 오른쪽으로 하나씩 이동하며 원래 순열에 대한 순서를 지켜주면서,
#     for j in range(i):
#         if l[j] < l[i]: # 부분 수열 내에서 증가하는 순서를 지키도록 조건을 걸어준다.
#             dp[i] = max(dp[j]+1, dp[i]) # 일단 위의 조건에서 l[j]보다 현재 가지고있는 수(l[i])가 크다는건 확인이 되었으니,
#                                         # dp[j] 즉, l[j]를 마지막 원소로 하는 부분 수열의 최대길이에서
#                                         # 현재 가지고 있는 수를 그 부분 수열 끝에 추가해준 길이(dp[j]+1) 중(j는 0부터 i-1까지 가능) 중
#                                         # 가장 큰 값을 dp[i]로 갱신한다.

# print(max(dp))
# # 원래 수열의 각 원소를 마지막 원소로 가지는 부분수열의 길이(dp의 원소값) 중 최대값을 출력하면 된다.
           
# 2. O(nlog n)
# https://seungkwan.tistory.com/m/8
# dp[i] 는 길이 i+1의 부분수열이 가질 수 있는 마지막 값 중 가장 작은 값이다.
# 일단 dp[0] 을 원래 수열의 첫째 값으로 초기화한다. 어차피 다 최소값으로 갱신될 것이다.
n = int(input())
l = list(map(int, sys.stdin.readline().split()))

def go(l):
    dp = [l[0]]

    for a in l[1:]:
        i = bi_lower_bound(dp,a)
        if i == len(dp)-1 and dp[i] < a:    # 마지막 인덱스가 반환되었으면.
            dp.append(a)
        else:
            dp[i] = a
    
    return len(dp)

def bi_lower_bound(l, key):
    left, right = 0, len(l)-1
    
    while left < right:
        mid = (left + right) // 2
        
        if key <= l[mid]:
            right = mid
        else:
            left = mid + 1
            
    return right

print(go(l))