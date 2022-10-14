# 55032KB 512ms
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def lcs():
    subs_one = list(map(str, list(input().rstrip())))
    subs_two = list(map(str, list(input().rstrip())))
    matrix = [[0] * (len(subs_two)+1) for _ in range(len(subs_one)+1)]
    # 각 문자열의 일치여부를 비교할 matrix

    for i in range(1, len(subs_one)+1):
        for j in range(1, len(subs_two)+1):
            # 2중 반복문을 통해 일치여부를 쭉 확인한다.
            
            if subs_one[i-1] == subs_two[j-1]:
                # 마지막으로 들어온 문자가 일치한다면?
                # 인덱스도 -1을 한 이유는 위에 matrix에서의 비교하기 위해 (0) 배열을 비워놓기 위해 1씩 추가해서 길이가 7인데
                # 문자열은 길이가 6이라서 -1을 하지않으면 out of index가 발생한다.
                matrix[i][j] = matrix[i-1][j-1] + 1
                # 그 전의 LCS에서 +1을 한다.
                # 이유가 뭐냐면 예를 들어 두 문자열 AB와 ACB를 비교한다고 생각해보자.
                # 둘이 서로 마지막 글자인 B가 들어오기전 둘의 LCS는 A로 길이가 1이었다.
                # 하지만 B가 들어오면서 LCS는 AB가 되었고 A보다 1이 길어지게 된다.
                # 1을 더하는 이유는 당연히 한 글자씩 비교하기 때문에 이것까지 설명할 필요는 없다.
            else:
                # 마지막으로 들어온 문자가 일치하지 않는다면?
                matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j])
                # 각 문자열의 마지막 문자가 추가되기 전애서 가장 큰 숫자가 lcs의 숫자가 된다.
                # 이유가 뭐냐면 아까 예를 조금 변형해서 문자열 AB 와 문자열 ABC를 비교한다고 생각해보자.
                # 둘이 서로 마지막 글자가 B와 C로 다르기 때문에 기존 LCS에서 무조건 1이 추가되는 건 불가능하다.
                # 그러면 첫번째 시퀀스에서 마지막 글자를 뺀 A와 두번째 시퀀스 ABC를 비교하고 첫번쨰 시퀀스 AB와 두번째 시퀀스에서 마지막 글자를 AB를 비교하여 그 중 가장 길이가 긴게 LCS가 될 것이다.
                # 그래서 [i-1][j]를 하는 거고 [i][j-1]을 하는 것이다.
                # 결국 A와 ABC의 LCS는 A로 길이가 1이 될 것이고, AB와 AB의 LCS는 AB로 길이가 2가 될 것이다. 이중 최대 길이는 AB로 LCS의 길이는 2가 될 것이다.

    print(matrix[-1][-1])
    # (왜 -1과 -1 인덱스를 출력하냐면 우리가 가져올 값은 매트릭스의 가장 마지막 값이기 때문이다. 모든 문자열을 비교한 결과값이 누적되어 [i][j]의 값에 저장이 되는데, 입력값을 매번 다르게 받기 때문에 인덱스를 -1로하면 무조건 마지막 열의 마지막 행의 값에 접근할 수 있게되고 정답을 확인할 수 있다.)


lcs()
