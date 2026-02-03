# 최대 집의 수 26, 최대 치킨 집의 수 13
# 치킨 집중에서 (치킨 집 수 - m개)만큼 뺀 이후 최소 거리를 구한다. 총 집의 갯수만큼 나온다.

import sys
from itertools import combinations

input = sys.stdin.readline

def main():

    m, house, chicken, answer = [], [], [], []
  
    N, M = map(int,input().split())

    for _ in range(N):
        m.append(list(map(int,input().split())))

    for i in range(N):
        for j in range(N):
            if m[i][j] == 1:
                house.append((i,j))
            elif m[i][j] == 2:
                chicken.append((i,j))
              
    com = combinations(chicken, M)
    # combinations(chicken, 3)의 결과물 예시
    # com = [
    #     ((0, 1), (2, 3), (4, 5)),  # 첫 번째 덩어리
    #     ((0, 1), (2, 3), (9, 9)),  # 두 번째 덩어리
    # ]

    for a in com:
        bf = 0
        for i, j in house:
            n = float('inf')
            for k, l in a:
                n = min(n, (abs(i - k) + abs(j - l)))
            bf += n
        answer.append(bf)
        
    return min(answer)

if __name__ == '__main__':
    print(main())
