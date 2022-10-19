import sys
sys.stdin = open("W03-W04/Week04/1946/input.txt","r")

# 배열을 이용한 방법.
# 필요한 크기의 배열을 미리 만들어 놓고, x값을 인덱스로 삼아 y값을 저장하면 x에 대해서 입력과 동시에 정렬이 되는 방식. 효율적.
for _ in range(int(input())):
    n = int(input())
    l = [0] * (n+1)
    for o in range(n):
        x,y = map(int, sys.stdin.readline().split())
        l[x]=y      # lesson pair 데이터의 한쪽에 대해 정렬을 해주고 싶다면 배열을 활용하면 좋다.
    min_=100_001
    cnt = 0
    for i in range(1,len(l)):
        if  l[i] < min_:  # 쌓인 등수의 최소보다 더 작아야(등수가 높아야) 함.
            min_ = l[i]
            cnt += 1
    print(cnt)

# 입력값을 정렬 후 수행.
# for _ in range(int(input())):
#     l = sorted([tuple(map(int, sys.stdin.readline().split())) for o in range(int(input()))])
#     cnt = 0
#     min_ = 100_001 
#     for xy in l:
#         if  xy[1] < min_:  # 쌓인 등수의 최소보다 더 작아야(등수가 높아야) 함.
#             min_ = xy[1]
#             cnt += 1
#     print(cnt)
    
# heap을 이용한 방법.
# 하지만 문제를 풀기 위해선 여태까지의 y들을 모두 가지고 있을 필요 없이, 항상 최소의 y만 갱신해서 가지면 되므로 비효율적.
# from heapq import heappush
# import sys

# for _ in range(int(input())):
#     l = sorted([tuple(map(int, sys.stdin.readline().split())) for o in range(int(input()))])
#     hq = [100_001]
#     cnt = 0
#     for xy in l:
#         if  xy[1] < hq[0]:  # 쌓인 등수의 최소보다 더 작아야(등수가 높아야) 함.
#             cnt += 1
#         heappush(hq, xy[1])
#     print(cnt)