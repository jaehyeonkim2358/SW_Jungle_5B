import sys
sys.stdin = open("input.txt","r")
# 12. https://www.acmicpc.net/problem/1931: 회의실 배정
# input = sys.stdin.readline

# 회의실 한개의 n개의 회의에 대한 사용표
# 회의 최대 개수
n = int(input())

arr = []
for _ in range(n):
    a, b = map(int,input().split())
    arr.append((a, b))

# 끝나는 시간을 오름차순으로 정렬 했기 때문에 앞에 꺼만 보면 된다. 
# 시작 시간을 오름차순으로 으로 정렬하는건 만약, (9,9)와 (8,9)가 있다고 가정하면
# 겹치게 되어 카운팅이 안되는데, 실제로는 1번이 카운팅이 되어야 한다. 
'''11
1 4
3 5
0 6
5 7
3 8
9 9
8 9
8 11
11 12
2 13
12 14'''
    
# arr = sorted(arr, key=lambda x: x[0]) #요건 생각 못했다..
arr = sorted(arr, key=lambda x: (x[1], x[0])) 

print(arr)

count1 = 0
check = 0
for i in range(n):
    if check <= arr[i][0]:
        count1 +=1
        check = arr[i][1]

print(count1) 