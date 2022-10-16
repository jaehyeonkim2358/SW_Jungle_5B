import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
_map = [list(map(int, input().split()))for _ in range(n)]
dp = [[0] * (1 << n-1) for _ in range(n)]
# 해당 dp테이블의 존재는 해당 상황에서 최소 경로를 의미한다.
# 열은 현재까지 방문한 도시의 숫자를 의미한다. 예를 들어 도시의 개수(n)이 4라고 할 때 1<<n-1 = 1<<<3 = 1000이 될 것이다.
# 행은 도시의 개수이다


def tsp(to_, total_route):
    if dp[to_][total_route] != 0:
        return dp[to_][total_route]
        # 0이 아니라는 의미는 방문할 도시가 이미 방문한 적이 있다는 의미임.
        # 출발지 말고 재방문은 안됨
        # 해당 루트의 최솟값을 return함.

    if total_route == (1 << n-1) - 1:
        # (1 << n-1)  - 1의 의미는 모든 경로를 방문하였다는 의미이다. n이 4일 경우, 1000(2) - 1을 하면 111이 된다.
        if _map[to_][0] != 0:
            return _map[to_][0]
            # 방문할 도시가 마지막 도시이므로 다시 출발지로 돌아갈 길이 있는지?
            # 출발지가 0으로 설쟁해놓음 순환만 되면 출발을 어디서 하나 상관이 없기 때문 (원순열 특성)
            # 길이 있으면 해당 경로의 비용을 return함.
        else:
            return sys.maxsize
            # 돌아가는 길이 없기 때문에 이렇게 설정해 놓으면 만약에 다시 해당 경로를 타는 경우가 발생할 경우
            # 최솟값으로써 역할을 할 수 없는 값이 되도록 함.

    min_dist = sys.maxsize
    # 최솟값을 갱신하기 위해서 값을 할당한다.
    for city in range(1, n):
        # 순회할 도시의 순서를 선택해보자. 1부터 하는 이유는 우리는 출발을 0부터 해서 0으로 돌아올 것이고, 중간에 있는 경로만 생각할 것이기 때문이다.
        if not _map[to_][city]:
            continue
            # 방문할 도시에서 다음으로 갈 도시가 길이 있다면 int 없다면 0이 있을 것이다.
            # 만약에 길이 없다면 더 이상 의미 없는 경로이다.
        if total_route & (1 << city - 1):
            continue
            # 지금까지 방문한 전체의 길과 다음으로 갈 도시와 and 연산을 함.
            # 만약에 n = 4인 경우 total_route = 110(2)(2,3번 도시 방문), (1 << city -1) = city의 번호를 이진수로 만드는 것이다.
            # city가 2인 경우 1 << 2-1 = 1 << 1 = 10(2)이 된다.
            # and 연산을 하게 될 경우 비교하는 두 이진수 각 자리수 중 둘 다 같으면 1 아니면 0이 된다.
            # 예를 들면 110(2)과 001(2)을 비교하면 둘다 다르므로 0이 나와 false가 될 것이다. 이는 곧 방문할 도시가 기존에 방문한 적이 없다는 것을 의미한다.
            # 반대로 110(2) 와 010(2)를 비교하면 010(2)가 될 것이고 True가 될 것이다, 이는 곧 방문할 도시가 기존에 방문한 명단에 있다는 것을 의미한다. 이미 방문한 적을 다시 방문할 수는 없기 때문에 의미 없는 경로가 될 것이다.

        distance = _map[to_][city] + tsp(city, total_route | (1 << city-1))
        # 다음으로 갈 도시가 있고 방문한 적이 없던 도시였으면 다시 다음 도시로 넘어가서 계산을 해야 한다.

        if min_dist > distance:
            min_dist = distance
            # 해당 경로가 최솟값이라면 갱신해준다.

    dp[to_][total_route] = min_dist
    # to_까지 왔을 떄 / total_route : 지금까지 방문한 도시들

    return dp[to_][total_route]


print(tsp(0, 0))
# 출발지 0, 현재까지 방문한 도시 숫자
