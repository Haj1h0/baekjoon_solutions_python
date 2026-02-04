# 코테에서 흔히 쓰는 백트래킹(DFS)으로 벽 3개 세우기 + BFS로 바이러스 확산 정석 버전 
import sys
from collections import deque

input = sys.stdin.readline
DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

def spread_and_count_safe(lab, N, M, viruses):
    q = deque(viruses)
    while q:
        x, y = q.popleft()
        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and lab[nx][ny] == 0:
                lab[nx][ny] = 2
                q.append((nx, ny))
    return sum(row.count(0) for row in lab)

def main():
    N, M = map(int, input().split())
    base = [list(map(int, input().split())) for _ in range(N)]

    empties = []
    viruses = []
    for i in range(N):
        for j in range(M):
            if base[i][j] == 0:
                empties.append((i, j))
            elif base[i][j] == 2:
                viruses.append((i, j))

    best = 0

    def backtrack(start_idx, walls_left):
        nonlocal best

        # 벽 3개 다 세웠으면 시뮬레이션
        if walls_left == 0:
            lab = [row[:] for row in base]  # 복사
            best = max(best, spread_and_count_safe(lab, N, M, viruses))
            return

        # 남은 빈칸에서 조합처럼 고르기 (중복 방지: start_idx부터)
        for idx in range(start_idx, len(empties)):
            x, y = empties[idx]
            if base[x][y] != 0:
                continue  # 이미 벽 세운 자리면 skip (사실상 안전장치)

            base[x][y] = 1              # 벽 세우기
            backtrack(idx + 1, walls_left - 1)
            base[x][y] = 0              # 되돌리기

    backtrack(0, 3)
    print(best)

if __name__ == "__main__":
    main()
