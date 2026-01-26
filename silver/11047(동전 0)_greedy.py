import sys

input = sys.stdin.readline

def main():

    cnt = 0 
  
    N, K = map(int, input().split())
    coin = [int(input()) for _ in range(N)]
    
    for i in sorted(coin, reverse=True):
       cnt += K // i
       K %= i
       if K == 0:    break

    return cnt
      
if __name__ == "__main__":
    print(main())

# 옛날 코드

# n, k = map(int,input().split())

# cl = []
# c = 0

# for _ in range(n):
#     coin = int(input())
#     cl.append(coin)

# cl.reverse()

# for i in cl:
#     c += k // i 
#     k = k % i
#     if k == 0:  break
    
# print(c)
