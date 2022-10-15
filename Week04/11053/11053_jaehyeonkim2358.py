# 가장 긴 증가하는 부분 수열(LIS; Longest Increasing Subsequence)

import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    nums = list(map(int, sys.stdin.readline().split()))
    dp = [nums[0]]                      # 수열의 첫번째 숫자를 넣어주고 시작
    for n in nums[1:]:                  # 수열의 두번째 숫자부터 순회
        index = binary_search(dp, n)    # 지금 숫자가 들어갈 수 있는 위치 탐색

        # 들어갈 수 있는 위치 = 마지막 인덱스일 경우, 
        # 원래 마지막 자리에 있던 숫자보다 크면 append() 해줌
        if index == len(dp)-1 and n > dp[-1]:
            dp.append(n)

        # 그 외에, 들어갈 위치의 숫자보다 지금 숫자가 더 작은경우
        # 원래 숫자 대신에 지금 숫자를 넣어줌
        elif dp[index] > n:
            dp[index] = n
            
        # else: dp 리스트에 갱신이 일어나지 않음
    sys.stdout.write(f'{len(dp)}')


def binary_search(_list, target):
    left = 0
    right = len(_list)-1
    while left < right:
        mid = (left + right) // 2
        if _list[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return right


main()