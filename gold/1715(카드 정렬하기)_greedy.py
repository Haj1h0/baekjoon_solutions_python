# 주어진 카드 묶음 중 가장 작은 두개의 묶음을 더하면서 모든 묶음이 묶일때까지 더한 횟수를 출력하는 문제
# 1. 가장 작은 두개의 묶음을 더한다.
# 2. 더한 묶음을 다시 묶음 리스트에 넣는다.
# 3. 묶음 리스트를 정렬한다.
# 4. 묶음 리스트의 길이가 1이 될때까지 반복한다.
# 5. 더한 횟수를 출력한다.
# 6. 종료

import heapq
import sys

# 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

heap = []
result = 0

for _ in range(int(input())):
    heapq.heappush(heap, int(input()))

while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    result += a + b
    heapq.heappush(heap, a + b)

print(result)  
