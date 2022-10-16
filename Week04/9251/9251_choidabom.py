# 9251: LCS
# LCS는 Longest Common Subsequence의 줄임말소 최장 공통 부분 수열이다. 
# 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

# 괜히 문제에서 입력값은 두 줄로 준게 아닌가 생각 한 번 해보고 ~
import sys
sys.stdin = open("9251/input.txt","r")
input = sys.stdin.readline

A = list(map(str, input().rstrip()))
B = list(map(str, input().rstrip()))

# 2차원 배열을 활용하여 두 문자열 매칭을 확인 
# for문 돌릴 때, i와 j가 0일 때는 0으로 초기화하려고 했는데 만들 때부터 애초에 0으로 초기화
LCS = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]

for i in range(1, len(A)+1): # ex) for i in range(1, 7) => 1~6
    for j in range(1, len(B)+1): # ex) for i in range(1, 7) => 1~6
        if A[i-1] == B[j-1]: 
            # A[i] == B[j]으로 했을 경우 list index out of range가 발생
            # ex) i=6, j=6 => A[6] == B[6] list index out of range가 발생
            # A와 B 배열의 크기는 6으로 index 0~5에 해당 
            
            # LSC 2차원 배열에서 비교하기 위해 (0) 배열을 비워놓기 위해 1씩 추가해서 길이가 7인데
            # 문자열 A, B의 길이는 6이기 때문에 -1 을 해줘야 한다. 
            # i=1, j=1 => A[1-1] == B[1-1] => A[0] = B[0], i=6, j=6 => A[6-1] == B[6-1] => A[5] = B[5]
            
            LCS[i][j] = LCS[i-1][j-1] + 1 # 문자가 같은 경우 대각선에 있는 친구에 +1
            # 그 전의 LCS에 +1을 한다.
            # 이유는 예를 들어 문자열 AB와 ACB를 비교한다고 생각해보자.
            # 둘이 서로 마지막 글자인 B가 들어오기 전 둘의 LCS는 A로 길이가 1이다.
            # 하지만 B가 들어오면서 LCS는 AB가 되었고 A보다 1이 길어지게 된다.
            # 1을 더하는 이유는 당연히 한 글자씩 비교하기 때문이다.
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1]) 
print(LCS[-1][-1])
    # (왜 -1과 -1 인덱스를 출력하냐면 우리가 가져올 값은 매트릭스의 가장 마지막 값이기 때문이다. 모든 문자열을 비교한 결과값이 누적되어 [i][j]의 값에 저장이 되는데, 입력값을 매번 다르게 받기 때문에 인덱스를 -1로하면 무조건 마지막 열의 마지막 행의 값에 접근할 수 있게되고 정답을 확인할 수 있다.)