import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/week04_Baekjoon/SW_Jungle_5B/input.txt","r")

n, k = map(int, sys.stdin.readline().strip().split())
# print(n, k)

plug_list = list(map(int, sys.stdin.readline().strip().split()))
# print(plug_list)

cnt = 0
plugin_list = [0] * n
# print(plugin_list)
search_idx = 0
tmp = 0
tmp_idx = 0
for plug in plug_list :
    # 플러그인에 이미 같은 게 있을 때 
    if plug in plugin_list :
        pass
    # 플러그가 아직 다 안 꽂혔다면
    elif 0 in plugin_list :
        plugin_list[plugin_list.index(0)] = plug

    # 다른게 꽂혀 있을 때
    else :
        for cur_plug in plugin_list :
            # 현재 꽂혀있는 게 더 이상 안 쓰이면
            if cur_plug not in plug_list[search_idx:] :
                tmp = cur_plug
                break
            # 현재 꽂힌 게 나중에도 사용됨(꽂힌 것들 중 여러개가 다시 사용된다면 더 나중에 사용되는 걸 뽑아야함)
            elif plug_list[search_idx:].index(cur_plug) > tmp_idx :
                # print(plug_list[i:].index(cur_plug))
                tmp = cur_plug
                tmp_idx = plug_list[search_idx:].index(cur_plug)
        plugin_list[plugin_list.index(tmp)] = plug  # plugin_list 수정
        tmp = 0
        tmp_idx = 0
        cnt += 1
    search_idx += 1 # 1개 탐색이 끝나면 search_idx +=1 
    
print(cnt)
