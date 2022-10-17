import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/week04_Baekjoon/SW_Jungle_5B/input.txt","r")

# 비트마스킹
# 컴퓨터는 내부적으로 모든 자료를 이진수로 표현합니다. 
# 이와 같은 특성을 이용해 정수의 이진수 표현을 자료구조로 쓰는 기법을 비트 마스크라고 합니다.
# 비트 마스크를 이용하면 더 빠른 수행 시간, 더 간결한 코드, 더 적은 메모리 사용이라는 효과를 얻을 수 있습니다.
# a & b : a의 모든 비트와 b의 모든 비트를 AND연산한다. / 둘다 1이라면 1, 아니면 0
# a | b : a의 모든 비트와 b의 모든 비트를 OR연산한다. / 둘다 0이라면 0, 아니면 1
# a ^ b : a의 모든 비트와 b의 모든 비트를 XOR연산한다. / 둘이 다르다면 1, 아니면 0
# ~a : a의 모든 비트에 NOT 연산을 한다. / 0이면 1, 1이면 0
# a << b : a를 b비트 만큼 왼쪽으로 시프트
    # ex) a = 1 = 001(2)
    #     a << 2 = 100(2) = 4
# a >> b : a를 b비트 만큼 오른쪽으로 시프트

####################################################################
# https://www.acmicpc.net/source/39573971 풀이 참고
####################################################################

# pos(현재위치) dest(마지막도착도시) bit(방문했던도시비트) visited(방문했던도시 set)
def solve(n) :
    inf = float('inf')
    cost = list(list(map(int, sys.stdin.readline().strip().split())) for _ in range(n))
    # print(cost)

    # dp는 현재 도시에서 남은 도시들을 거쳐 다시 출발점으로 돌아오는 비용
    # dp[i][1] = 현재 i도시이며, 방문현황은 1. 아직 방문하지 않은 도시들을 모두 거쳐 다시 시작점으로 오는데 드는 비용
    # 1번도시 bit : 0 / 2번도시 bit : 10 / 3번 도시 bit : 100
    dp = [[inf] * (1<<(n-1)) for _ in range(n)]
    # print(dp)

    # 이 과정은 왜 할까...........
    for i in range(n) :
        for j in range(n) :
            if not cost[i][j] :
                cost[i][j] = inf
    # print(cost)   # [[inf, 10, 15, 20], [5, inf, 9, 10], [6, 13, inf, 12], [8, 8, 9, inf]]

    # 이 과정은 왜 할까............
    for i in range(n) :
        dp[i][0] = cost[i][0]
    # print(dp)


    # 최소 비용 계산 함수
    def get_min(pos, visited) :
        ret = inf
        for city in range(1, n) :
            # i번 도시에 해당하는 비트
            # ex) city = 2 는 city = 10(2)
            city_bit = 1 << (city - 1)
            if visited & city_bit :
                # ex) visited = 110(2) --> visited & (~city) = 100(2)
                # 뒤쪽 수식의 의미 : pos에서 i번 도시를 지난 뒤
                # visited에서 i번 도시를 제외한 도시를 거친 후 0번 도시로 돌아갈 때의 비용
                # print(bin(visited), bin(~city_bit))
                # print(visited & (~city_bit))
                _cost = cost[pos][city] + dp[city][visited & (~city_bit)]
                # print(dp[city][visited&(~city_bit)])
                if ret > _cost :
                    ret = _cost
        return ret
 

    for visited in range(1, len(dp[0]) - 1) :
        for city in range(1, n) :   # city별로 visited를 돌려야하는거 아닌가.
            city_bit = 1 << (city - 1)
            # print(bin(city_bit), bin(visited))
            # print(city_bit & visited)
            if not city_bit & visited : # 둘 중 하나라도 false라면
                # print(city, visited)
                dp[city][visited] = get_min(city, visited)
    # print(dp)
    return get_min(0, len(dp[0]) - 1)


if __name__ == '__main__' :
    n = int(input())
    print(solve(n))