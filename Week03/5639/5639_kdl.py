import sys
sys.setrecursionlimit(10**6)
# 파이썬으로 재귀를 사용하여 문제를 해결할 때 런타임 에러가 발생함. 이는 파이썬의 재귀 최대 깊이의 기본 설정이 1000회이기 때문.
# sys.setrecursionlimit()을 통해 임의로 재귀의 깊이를 설정할 수 있음 > pypy는 안됨.
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def post_order(start, end):
    # start와 end는 arr의 시작 idx와 끝 idx임.
    if start > end:
        return
    # 순회는 재귀호출을 통해 자식노드를 순회하기 때문에 자식노드의 여부를 확인하여야 함.
    # child node가 없다는 것은 배열로 생각하면 본인 자신밖에 없다는 것을 의미함.
    root = pre_arr[start]
    # preorder는 root > left > right 순으로 순회하기 때문에 맨 처음에 나오는 value가 root node임.
    idx = start + 1

    while idx <= end:
        if pre_arr[idx] > root:
            break
        idx += 1
        # preorder의 특징은 root > left > rigt순으로 순회한다.
        # binary search tree의 특징은 left child는 root보다 작은 value가 들어가며 right child는 root보다 큰 숫자가 들어간다는 점이다.
        # 이러한 점을 이용하여 list에서 root보다 큰 숫자가 위치한 idx가 어디인지 확인할 수 있다.

    post_order(start+1, idx-1)
    # left node
    post_order(idx, end)
    # right node
    print(root)
    # 문제에서 요구하는 것은 입력으로 주어진 이진 검색트리를 후위순회 하는 것이다.
    # 해당 함수는 root와 left right를 구분했고 해당 함수를 left, right, root 순으로 다시 호출하여, 후위 순회를 완료하게 된다.


pre_arr = []
while 1:
    try:
        pre_arr.append(int(input()))
    except:
        break
# 입력되는 값의 개수가 정해지지 않았기 때문에 반복문을 통해서 값을 리스트에 입력받게 될 경우 별도의 종료 조건을 설정하여야 함.
# 예외처리를 하지 않으면 ValueError: invalid literal for int() with ~~ 가 발생되며 스크립트 실행이 중단됨.
# 따라서 이를 방지하기 위해 예외가 발생했을 때(except) 반복문을 종료하여 스크립트가 계속 실행되도록 함.

post_order(0, len(pre_arr)-1)
# 후위 순회를 실행한다.
