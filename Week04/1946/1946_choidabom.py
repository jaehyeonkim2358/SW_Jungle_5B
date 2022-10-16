# 1946: 신입사원
# 서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다는 원칙이 있다. 즉, 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않는다. 
import sys
sys.stdin = open("1946/input.txt","r")
input = sys.stdin.readline

T = int(input())
def solution():
    N = int(input())
    test = [tuple(map(int, input().split())) for _ in range(N)]
    test.sort() # 튜플로 들어갔기 때문에 서류 순으로 정렬
    cnt = 1
    # print(test)
    # [(1, 4), (2, 3), (3, 2), (4, 1), (5, 5)]
    # [(1, 4), (2, 5), (3, 6), (4, 2), (5, 7), (6, 1), (7, 3)]

    # sort()를 통해서 서류 심사 끝, 숫자는 등수이기 때문에 적은 수가 순위가 높음
    # 면접만 확인하면 됨.
    top = 0
    result = 1
    for i in range(1, N):
        # 순위이기에 1등의 면접결과(test[top][1])보다 면접결과(test[i][1])가 낮으면 cnt 안 함 
        if test[i][1] < test[top][1]:
            top = i 
            cnt += 1 # 서류심사 1등의 면접시험 성적보다 더 좋으면 count !
    print(cnt)

for _ in range(T):
    solution() 

