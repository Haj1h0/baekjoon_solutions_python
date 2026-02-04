# 벽 3개를 세워 안전영역의 최댓값을 구하는 문제
# 지도의 최대 크기는 8 * 8
# 모두 빈 칸일 경우 벽을 세울 수 있는 최대 경우의 수는 64 * 63 * 62 = 249,984 에다가 3! 나누기 = 41,664
# 1. 벽 3개를 넣는 방식
# 2. 벽 3개를 넣은 후 바이러스가 퍼진 이후 # 2. 벽 3개를 넣은 후 바이러스가 퍼진 이후 안전 영역의 크기 구하는 방식는 방식
import sys

input = sys.stdin.readline

def main():
    
    m, m_1, temp, max_safe = [], [], [], 0

    N, M = map(int,input().split())

    for _ in range(N):
        row = list(map(int, input().split()))
        m.append(row)
        m_1.extend(row) # 안전영역 중 3개에 벽을 넣기 위해 임의로 1차원 배열을 생성해준다.                      

    
    # 안전 영역의 크기 구하기 함수
    # 1_1. 위 아래 양 옆으로 갈 곳이 없거나 1혹은 2이면 해당 방향으로는 종료
    # 1_2. 위 아래 양 옆이 0이면 2로 변경
    # 2. 각각의 변경된 2에 대해서 1번 알고리즘 반복
    def change2(m : list, i : int, j : int, N, M):
        d = ((1,0),(0,1),(-1,0),(0,-1))
        # 해당 값이 2가 아닌 경우 종료
        if m[i][j] != 2:
            return
        for d1, d2 in d:
            # 바이러스가 이동할 영역이 연구소 영역 안에 있는 경우
            if (i + d1) < N and (j + d2) < M and (i + d1) >= 0 and (j + d2) >= 0:
                if m[i + d1][j + d2] == 0:
                    m[i + d1][j + d2] = 2
                    change2(m, i + d1, j + d2, N, M)
                    

    def size(temp, N, M):
        # 바이러스 퍼뜨리기
        for i in range(N):
            for j in range(M):
                if temp[i][j] == 2:
                    change2(temp, i, j, N, M)

        # 안전 영역의 크기 구하기
        return sum(row.count(0) for row in temp)

    
    for index_1, i in enumerate(m_1):
        if i == 0:
            temp1 = m_1[:]
            temp1[index_1] = 1
            if index_1 <= len(m_1) - 2:
                for index_2, j in enumerate(m_1[index_1 + 1:], start = index_1 + 1):
                    if j == 0:
                        temp2 = temp1[:]
                        temp2[index_2] = 1
                        if index_2 <= len(m_1) - 1:
                            for index_3, k in enumerate(m_1[index_2 + 1:], start = index_2 + 1):
                                if k == 0:
                                    temp3 = temp2[:]
                                    temp3[index_3] = 1
                                    temp3 = [temp3[i : i + M] for i in range(0, len(temp3), M)]
                                    max_safe = max(max_safe, size(temp3, N, M))

    
    return max_safe


if __name__ == '__main__':
    print(main())
