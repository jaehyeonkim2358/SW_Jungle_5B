from collections import deque
import sys
sys.stdin = open("W03/5639/input.txt","r")
sys.setrecursionlimit(10**6)
l = list(map(int, sys.stdin.read().strip().split('\n')))
# 문제의 의도 : 이진트리의 본질을 알자.
# "이진트리는 root의 왼쪽에는 root보다 작은 값들이 있고, root의 오른쪽에는 root보다 큰 값들이 있다."

def bi_search(s, e, key):   # 루트보다 작은 값 중에 가장 오른쪽에 있는 값의 위치를 알려주는 함수.
    while s < e:
        mid = (s+e)//2 + 1
        if l[mid] <= key:
            s = mid
        else: # key < l[mid]
            e = mid-1
            
    return s

def pre_to_post(l, s, e):
    if s > e : return
    elif s == e :
        print(l[s])
        return
    else: # s < e
        root = l[s]     # 입력값은 전위순회이기 때문에 항상 배열의 첫번째가 root이다.
        pivot = bi_search(s, e, root)   # 루트보다 값이 작은 것 중에 (배열에서)가장 오른쪽에 있는 값의 인덱스를 받아
                                        # 왼쪽 서브 트리의 범위를 설정할 수 있다. 
                                        # 왼쪽 서브트리가 없는 경우(1)를 대비해 루트의 인덱스 's'자체도 포함시켜준다.
                                        # 그러면 해당 경우에는 s가 다시 반환되게 된다.
                                        # 오른쪽 서브트리가 없는 경우(2)에는 e가 다시 반환되게 된다.
        
                                        # 아래에서는 서브트리가 메인 트리로 다시 호출되어 재귀적으로 실행된다.
                                        
        pre_to_post(l, s+1, pivot)      # 루트를 제외(s+1) 하고 왼쪽 서브트리의 범위(pivot)까지 다시 함수를 호출한다.
                                        # (1)의 경우에 pivot이 s이므로 함수 맨 처음 조건(s>e)의 조건에 걸려 아무것도 실행되지 않는다.
                                        # 즉, 왼쪽 서브트리가 없는 경우 왼쪽 서브트리에 대한 함수는 호출되지 않는 것이다.
                                        
        pre_to_post(l, pivot+1, e)      # 왼쪽 서브트리의 범위 다음 값 (pivot+1) 즉, 오른쪽 서브트리의 루트부터
                                        # 오른쪽 서브트리의 범위(e)까지 다시 함수를 호출한다.
                                        # (2)의 경우에 pivot이 e이므로 역시 함수 맨 처음 조건(s>e)의 조건에 걸려 아무것도 실행되지 않는다.
                                        # 즉, 오른쪽 서브트리가 없는 경우 왼쪽 서브트리에 대한 함수는 호출되지 않는 것이다.

        print(root)                     # 후위순회이기 때문에 root를 가장 마지막에 출력해준다.
        
pre_to_post(l,0,len(l)-1)