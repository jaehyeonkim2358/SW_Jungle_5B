from sys import stdin

stdin = open("input.txt","r")
input=stdin.readline

n,k=map(int,input().split())   # n : 물품의 수 / k : 무게 한계

#다음 줄 부터 각 물품의[무게, 가치]를 받는다 , 그리고 무게를 기준으로 정렬한다.--------------

product=[[0]]
for i in range(n):                                  #[[0],[6, 13], [4, 8], [3, 6], [5, 12]]
    product.append(list(map(int,input().split())))

product.sort(key=lambda x:x[0])                     #[[0], [3, 6], [4, 8], [5, 12], [6, 13]]  

#----------------------------------------------------------------

dp_table=[[0]*(k+1) for _ in range(n+1)]  

for i in range(1,n+1):
    for j in range(1,k+1):
        tmp_weight=product[i][0]
        tmp_val=product[i][1]
        if tmp_weight>j:
            dp_table[i][j]=dp_table[i-1][j]
        else:
            dp_table[i][j]=max(dp_table[i-1][j],(tmp_val+dp_table[i][j-tmp_weight]))
            
print(dp_table[n][k])
