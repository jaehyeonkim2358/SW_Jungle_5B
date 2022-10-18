import sys
sys.stdin = open("W03-W04/Week04/1931/input.txt","r")
n = int(input())
l = []
for _ in range(n):
    l.append(tuple(map(int, sys.stdin.readline().split())))
l.sort(key=lambda x :(x[1], x[0]))  # end가 같은 것끼리 start값(x[0]) 오름차순 안해주면 걸리는 반례 : [(8,8), (7,8)]

def go_by_linear(n, l):
    cnt = 0
    prev_end = -1
    for i in range(n):
        start = l[i][0]
        if prev_end <= start:
            cnt += 1
            prev_end = l[i][1]
        else:
            continue
        
    return cnt
                
print(go_by_linear(n,l))  

# 현재의 end보다 큰 다음의 start를 이분탐색으로 찾고자 했으나 삽질.
# 배열 l은 각각의 end값에 대해 오름차순으로 정렬되어있지, start값에 대해서는 정렬된 상태를 보장하지 않는다. 다만 같은 end안에서의 start끼리의 오름차순을 보장할 뿐이다.
# 따라서 반례가 쉽게 생긴다.
# 이분탐색은 배열 전체가 정렬된 상태일 때 사용해야 한다는 것을 다시 한 번 명심하자.
#
# def lower_bound(l, lo, key): 
#     left=lo ; right=len(l)-1
#     while left < right:
#         mid = (left+right)//2
#         if key <= l[mid][0]:
#             right = mid
#         else:
#             left = mid + 1

#     return right

# def go_by_bisearch(n, l):
#     cnt = 0
#     i = -1
#     end = -1
#     while True:
#         i = lower_bound(l, i+1, end)
#         if i == n-1:   # 끝 인덱스에서의 판단. 이진 탐색이 반환할 수 있는 최대 값은 n-1값 밖에 없어 따로 판단을 해주어야함.
#             if end <= l[i][0]:
#                 cnt += 1
#             break
            
#         end = l[i][1]
#         cnt += 1
        
#     return cnt   
# print(go_by_bisearch(n,l))     