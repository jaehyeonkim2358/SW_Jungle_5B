import sys


def solution(depth, result):
    global min_result
    global max_result

    # 탐색 깊이가 전체 숫자의 갯수(n)만큼 깊어지면 탐색 종료
    if depth == n:
        max_result = max(max_result, result)        # 최대값 갱신
        min_result = min(min_result, result)        # 최소값 갱신
        return

    cur = num_list[depth]   # 현재 순서의 숫자
    # r0 ~ r3까지 4가지 연산의 결과값 저장
    r0 = result + cur
    r1 = result - cur
    r2 = result * cur
    r3 = (result // cur) if (result >= 0) else -(-result // cur)

    for i in range(4):
        # 사용 가능한 연산자 선택
        if operator[i] > 0:
            operator[i] -= 1                        # 사용 가능 횟수 1감소
            next_result = [r0, r1, r2, r3][i]       # 현재 선택한 연산자(i)를 사용했을 때의 결과값을 다음 호출로 전달
            solution(depth+1, next_result)
            operator[i] += 1                        # 탐색 종료 후 사용 가능 횟수 복구


n = int(sys.stdin.readline().rstrip())                      # 숫자의 갯수
num_list = list(map(int, sys.stdin.readline().split()))     # 숫자 리스트
operator = list(map(int, sys.stdin.readline().split()))     # 연산자 갯수(순서: +, -, *, /)

# 연산 결과로 나올 수 없는 값으로 최대값, 최소값 초기화
min_result = 1000000001
max_result = -1000000001

# 첫번째 숫자를 전달하며 시작
solution(1, num_list[0])

# 최대값, 최소값 출력
sys.stdout.write(f'{max_result}\n{min_result}')