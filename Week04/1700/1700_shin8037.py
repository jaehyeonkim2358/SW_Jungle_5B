import sys

input=sys.stdin.readline
N,k=map(int,input().strip().split())
items=list(map(int,input().strip().split()))

multitap=[None]*N
count=0
maximum=temp=0

while items:
    i=items[0] # 항상 제일 앞에 있는 것을 사용해야하기 때문에
    if i in multitap:
        items.remove(i) # item이 이미 꽂혀있으니 리스트에서는 필요 X --> 삭제
        continue

    elif None in multitap: 
        multitap[multitap.index(None)]=i
        items.remove(i) # item을 꽂았으니깐 리스트에서 삭제

    else: # multitap이 꽉찼다면
        for used_item in multitap: # 멀티탭에 꽂힌 아이템을 돌리면서 -- 이 for문의 역할을 이중에서 제거해야할 것을 찾는거
            # 남은 아이템에서 없다면 제거 1순위
            # 만약 남은 아이템에 있다면 가장 나중에 사용될 애들 미리 뽑는다는 의미
            if used_item not in items: # 사용된 아이템이 남은 아이템중에서도 없다면
                temp=used_item # 가장 먼저 뽑아야할 애니깐 위치를 기억하기 위해서 내용을 저장해놓음
                break # 얘는 찾으면 그냥 중지하고 바로 뽑아도됨
                
            elif items.index(used_item)>maximum: # 사용된 아이템의 인덱스(즉 사용순서가) 앞에서 뺐던 애들보다 더 뒤에 있는지
                maximum=items.index(used_item) # 그렇다면 얘의 index를 최대 max로 등록
                temp=used_item # 이 아이템을 temp에 저장
        multitap[multitap.index(temp)]=i # 멀티탭에 아이템을 꽂는다
        items.remove(i) # 아이템에서 방금 꽂은거 제거
        maximum=0 # 다시 maximum 초기화
        count+=1 # 콘센트 뽑은 횟수 추가

print(count)
