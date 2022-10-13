#01타일

# 지원에게 2진 수열을 가르쳐 주기 위해 지원이 아버지는 그에게 타일들을 선물해주셨다. 그리고 이 각각의 타일들은 0 또는 1이 쓰여 있는 낱장의 타일들이다.
# 0이 쓰여진 낱장의 타일들을 붙여서 한 쌍으로 이루어진 00타일들을 만들었다.
import sys
read = sys.stdin.readline

N = int(read())
cache = [0] * (N+2)
cache[1] = 1
cache[2] = 2

for i in range(3, N+1):
    cache[i] = (cache[i-1] + cache[i-2]) % 15746
print(cache[N])