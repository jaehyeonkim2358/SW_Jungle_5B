import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/week04_Baekjoon/SW_Jungle_5B/input.txt","r")

t = int(input())
for _ in range(t) :
    n = int(input())
    res_list = []
    for _ in range(n) :
        res_list.append(list(map(int, sys.stdin.readline().strip().split())))

    res_list.sort(key = lambda x : x[0])
    # print(res_list)

    top = 0
    cnt = 1 
    # 이미 sort를 통해서 서류심사 비교는 끝났기 때문에 top값만 저장해놓고 비교하면 됨.
    for i in range(1, n) : # idx 0은 이미 들어가 있다고 가정하기 때문에 idx 1부터 탐색
        if res_list[i][1] < res_list[top][1] :
            top = i     
            cnt += 1

    print(cnt)
