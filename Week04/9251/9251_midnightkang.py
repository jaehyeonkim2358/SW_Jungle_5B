from sys import stdin

stdin = open("input.txt","r")
input=stdin.readline

x=input().strip()
y=input().strip()

x_list=[0]+list(x)
y_list=[0]+list(y)

dp_table=[]
for i in range(len(y)+1):
    dp_table.append([0]*(len(x)+1))

print(dp_table)
for i in range(len(x)+1):
    for j in range(len(y)+1):
        if x_list[i]==y_list[j]:
            dp_table[i][j] = dp_table[i-1][j-1]+1
        else:
            dp_table[i][j]=max(dp_table[i][j-1],dp_table[i-1][j])
            
print(dp_table[-1][-1])
