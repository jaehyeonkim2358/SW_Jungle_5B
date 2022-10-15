n = int(input())

# top-down
# dp table
d = [0] * (n+1)

def fibo(n):
    if n < 3 :
        return 1
    
    if d[n] != 0:
        return d[n]

    d[n] = fibo(n-1) + fibo(n-2)
    
    return d[n]

print(fibo(n))

# bottom-up
# dp-table
d = [0] * (n+2)     # (n+1)이 아닌 이유: n이 1인 경우에 23번줄에서 index error가 나지 않도록 한칸의 여유를 더 둔다.
d[1] = d[2] = 1

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
print(d[n])