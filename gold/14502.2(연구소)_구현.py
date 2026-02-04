# (조합 + BFS)
import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

def spread_and_count_safe(lab, N, M, viruses):
    """lab를 직접 변형시키며 바이러스 확산 후 안전영역(0) 개수 반환"""
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

    for walls in combinations(empties, 3):
        # ✅ 매 케이스 행 단위 복사(빠르고 충분)
        lab = [row[:] for row in base]

        # ✅ 벽 세우기
        for x, y in walls:
            lab[x][y] = 1

        # ✅ 바이러스 확산 + 안전영역 계산
        best = max(best, spread_and_count_safe(lab, N, M, viruses))

    print(best)

if __name__ == "__main__":
    main()
