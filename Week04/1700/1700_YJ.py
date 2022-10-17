import sys
sys.stdin= open("input.txt","r")
input= sys.stdin.readline

N,K= map(int, input().split())
seq = list(input().strip().split())
outlets= [None for _ in range(N)]
cnt= 0 # 총 빼는 횟수 
    
for i in range(K):
    item = seq[i]
    if item in outlets: # 이미 꽃혀있는 경우
        continue # 다음 물건 사용하러 가면 된다
    try :
        available = outlets.index(None) 
    except: 
        available = -1

    if available >= 0 :  #남는 자리가 있는 경우 
        outlets[available]= item
    else : # 남는 자리가 없는 경우
        # 현재 꽂혀있는 물걸들이 남은 배열에서 몇번째에 나오는지 확인 후 수가 큰 순서대로 뺀다 
        # 남은 배열에서 안 나오면 젤 큰수 K+1로 넣어준다
        biggest = -1
        for j in range(N) :
            item_in_use = outlets[j]
            try : 
                temp = seq.index(item_in_use,i+1) #i+1 자리 부터 끝까지 찾는다! 있으면 인덱스가 없으면 -1이 반환 될 것 
            except :
                temp = K+1
            if biggest < temp :
                biggest = temp 
                biggest_item = j
        outlets[biggest_item] = item  #biggest_item 를 빼고 아이템을 집어넣는다!
        cnt += 1 

print(cnt)
