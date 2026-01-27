# N과 K의 MAX가 300,000 이기에 한번의 scan안에서 최적의 greedy 방법을 찾는다.
# 작은 가방부터 타깃으로 채울 수 있는 비싼 보석 하나씩 넣는다. 

# 1 65
# 5 23
# 2 66
# 3 99
# 10
# 3
# 2

# 가방 2 주목, 가방 2에 들어올 수 있는 무게의 보석 정보 모두 heap에 저장 후 최대 무게 pop(-통해서)
# 가방 3 주목, 가방 3에 들어올 수 있는 무게의 보석 정보 모두 heap에 저장 후 최대 무게 pop(-통해서)
# 가방 10 주목, 가방 10에 들어올 수 있는 무게의 보석 정보 모두 heap에 저장 후 최대 무게 pop(-통해서)
# 가방이 너무 작어서 들어온 보석이 없는 경우도 처리
# 가방이 남아도 보석이 없는 경우도 처리

import sys, heapq

input = sys.stdin.readline
  
def main():

    max_price, val = 0, 0
    hq = []
  
    N, K = map(int,input().split())
    J = [tuple(map(int,input().split())) for _ in range(N)]
    B = [int(input()) for _ in range(K)]
    J.sort()
  
    for i in sorted(B):                      # 처음에 런타임 에러 val < N 체크가 뒤에 있어서 방어가 안 됐음,  while val < N and J[val][0] <= i:
        while val < N and J[val][0] <= i:    # val < N 통해 가방이 남아도 보석이 없는 경우도 처리     
            heapq.heappush(hq, -J[val][1])    # 최대 무게를 꺼내야하기에 음수 변환
            val += 1
        if hq:
            max_price -= heapq.heappop(hq)    
  
    return max_price

if __name__ == '__main__':
    print(main())

# 처음에 런타임 에러 val < N 체크가 뒤에 있어서 방어가 안 됐음,  while val < N and J[val][0] <= i:

# 보석 개수 : N, 보석 무게 : M, 보석 가격 : V, 가방 개수 : K, 가방 최대 무게 : C
# import heapq
# import sys

# input = sys.stdin.readline

# def main():

#   jewelry, bags = [], []
#   answer = 0

#   N, K = map(int, input().split())

#   for _ in range(N):
#       M, V = map(int, input().split())    # 보석 무게, 보석 가격
#       jewelry.append((M, V)) 
#   jewelry.sort(key = lambda x : x[1], reverse = True)    # 보석 가격이 큰 순으로 정렬

#   for _ in range(K):
#       heapq.heappush(bags,int(input()))    # 가방 최대 무게가 작은 순으로 정렬

#   while bags:
#       bag = heapq.heappop(bags)
#       for i in range(len(jewelry)):  
#           if jewelry[i][0] <= bag:
#               answer += jewelry[i][1]
#               jewelry.pop(i)  
#               break

#   return answer

# if __name__ == "__main__":
#      main()

# 최초 아이디어 1) 보석의 무게와 가격이 적힌 튜플을 가격이 큰 순으로 정렬한 후 작은 가방부터 1개씩 넣어보면서 최대 가격을 확인한다.
# 1. 보석 (무게, 가격) 리스트를 가격 내림차순으로 정렬
# 2. 가장 비싼 보석을 타깃으로 맞추고 가방을 작은 용량부터 하나씩 보면서
# 3. “현재 가장 비싼 보석(타깃 보석)”이 이 가방에 들어가면 담고(정답에 더하고)
# 4. 보석/가방 리스트에서 삭제하고 다음으로 진행

# 아이디어 2) 가방을 작은 무게 순으로 정렬하고 해당 가방에 맞는 가장 높은 가격의 보석을 넣는다.
# 1. 가방 리스트를 무게 오름차순으로 정렬
# 2. 가장 작은 가방부터 보석 리스트를 돌면서 가방에 넣을 수 있는 가장 비싼 보석을 넣는다.
# 3. 넣은 보석은 보석 리스트에서 삭제하고 다음 가방으로 넘어간다.
# 4. 만약 가방에 넣을 수 있는 보석이 없으면 넘어간다.
# 5. 모든 가방에 대해 반복한다.


