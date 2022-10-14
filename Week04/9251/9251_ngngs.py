import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/week04_Baekjoon/SW_Jungle_5B/input.txt","r")

# LCS알고리즘 https://chanhuiseok.github.io/posts/algo-34/
# 사고 포인트 : 기준 문자열을 두고, 비교 문자열을 가져와서 앞에서 부터 비교
# 비교했을 때 달랐을 경우, 왼쪽의 값과 위쪽의 값 중 더 큰 값을 현재 위치에 씁니다.

insert_val = sys.stdin.readline().strip()
insert_val2 = sys.stdin.readline().strip()
# print(insert_val, insert_val2)

val_length = len(insert_val)
val_length2 = len(insert_val2)

dp = [[0] * (val_length2 + 1) for _ in range(val_length+1)] # 2차 함수 만들기

for i in range(1, val_length+1) :
    for j in range(1, val_length2+1) :
        if insert_val[i-1] == insert_val2[j-1] :
            dp[i][j] = dp[i-1][j-1] + 1
        else :
            dp[i][j] = max(dp[i][j-1], dp[i-1][j]) # 왼쪽 대각선 위 혹은 바로 위 값 중 더 큰 값

print(dp[val_length][val_length2])