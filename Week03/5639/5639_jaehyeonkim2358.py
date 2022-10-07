import sys
# 재귀 호출 횟수 제한을 꼭 설정해주어야 함
sys.setrecursionlimit(14000)
input = sys.stdin.readline
print = sys.stdout.write

pre = []

while True:
    try:
        pre.append(int(input().rstrip()))
    except:
        break


def solution(root_index, end):
    if root_index > end:
        return
    if root_index == end:
        print(f'{pre[root_index]}\n')
        return
    m = binary_search(root_index+1, end, pre[root_index])
    solution(root_index+1, m-1)
    solution(m, end)
    print(f'{pre[root_index]}\n')


def binary_search(start, end, key):
    s = start
    e = end
    while s < e:
        m = (s + e) // 2
        if pre[m] > key:
            e = m
        else:
            s = m + 1
    return e if pre[e] > key else e+1


solution(0, len(pre)-1)