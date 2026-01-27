# N(MAX) = 200,000 -> 이중 for문 X 특정 순서대로 정렬한 채, 원소 하나씩 체크하면서 greedy한 방법 찾아내자
# 그렇기 위해서는 스캔하면서 현재 진행 중인 강의들을 어딘가에 쌓아두고 관리해야 한다.
# 스캔 중 현재 사용 중인 강의실들 중 ‘종료시간의 최솟값’에 주목한다.
# (1 13)
# (2 7)
# (2 5)
# (6 8)
# (8 9)
# (9 12)
# heap[0]과 시작 시간 비교를 통해 heappop을 결정하고 heappush는 무조건 수행된다.
# 1) -> 13 (heap = [] 이면 heap push를 진행한다. heappush -> heap[0] = 13, lenheap = 1) 
# 2) -> 7 (heap[0] > 시작 시간(2) 이기에 heappop은 진행 x, heappush -> heap[0] = 7, lenheap = 2) 
# 3) -> 5 (heap[0] > 시작 시간(2) 이기에 heappop은 진행 x, heappush -> heap[0] = 5, lenheap = 3)
# 4) -> 8 (heap[0] <= 시작 시간(6) 이기에 heappop 1번 진행 후 heappush -> heap[0] = 7, lenheap = 3)
# 5) -> 9 (heap[0] <= 시작 시간(8) 이기에 heappop 2번 진행 됨 heappush -> heap[0] = 9, lenheap = 2)
# 6) -> 12 (heap[0] <= 시작 시간(9) 이기에 heappop 1번 진행 됨 heapush -> heap[0] = 12, lenheap = 2) 

import heapq
import sys

input = sys.stdin.readline

def main():

    hq = []
    m = 0
  
    room = [tuple(map(int,input().split())) for _ in range(int(input()))]
    room.sort(key = lambda x : (x[0], -x[1]))

    for x, y in room:
        if not hq:    
            heapq.heappush(hq, y)
            m = len(hq)
            continue
        while hq[0] <= x:
            heapq.heappop(hq)
        heapq.heappush(hq, y)
        m = max(m, len(hq))
  
    return m
      
if __name__ == "__main__":
    print(main())


# import sys, heapq
# input = sys.stdin.readline

# def main():
#     n = int(input())
#     lectures = [tuple(map(int, input().split())) for _ in range(n)]
#     lectures.sort()  # start 오름차순, start 같으면 end 오름차순

#     hq = []
#     for s, e in lectures:
#         if hq and hq[0] <= s:   # 가장 빨리 끝나는 강의실 재사용 가능
#             heapq.heappop(hq)   # 방 1개만 비우고
#         heapq.heappush(hq, e)   # 새 강의 배정

#     return len(hq)              # 처리 후 힙 크기 = 필요한 최소 강의실 수

# if __name__ == "__main__":
#     print(main())
