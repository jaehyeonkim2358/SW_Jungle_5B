# https://www.acmicpc.net/problem/1700


N, K = map(int, input().split())
scheduling = list(map(int,input().split()))
# print(scheduling) [2, 3, 2, 3, 1, 2, 7]
adaptor = [0] *N
count = 0
scheduling_idx = 0
tmp = 0
tmp_i = 0

for i in scheduling:
  
  # 멀티탭에 같은 전기 용품이 있을 때
  if i in adaptor:
    pass

  # 멀티탭이 아직 채워지지 않았을 때, adpator가 0인놈 index찾아서 그 index에 i를 넣어줌
  elif 0 in adaptor:
    a=adaptor.index(0)
    adaptor[adaptor.index(0)]= i

  # 멀티탭에 빈자리 없고 현재 꽂혀 있는 전기용품들과 다를 때
  else:
    for j in adaptor: #2,3
      # print(scheduling[scheduling_idx : ])

      # 현재 꽂혀있는 전기용품이 더이상 사용되지 않는다면?
      if j not in scheduling[scheduling_idx: ]:
        tmp = j #tmp는 뽑힐 가능성이 있으면 tmp에 올리는거야..
        
        break
      # 꽂혀있는 전기용품이 이후에도 사용될 때 (2는 5번째에 또 사용 된다)
      else:
        a =scheduling[scheduling_idx : ]
        if a.index(j) > tmp_i: # 꽂혀있는 것들 중 여러 개가 다시 사용될 때, 더 나중에 사용되는 것을 뽑는다.
          tmp = j
          tmp_i =a.index(j)
    adaptor[adaptor.index(tmp)] = i #여기서 플러그를 빼고 새로운 걸 넣는 행위를 함
    tmp=tmp_i =0
    count+=1
  scheduling_idx +=1
print(count)