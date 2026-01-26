N = int(input())

bl = [i for i in range(3,5001)]
cnt = 0
for i in range(N//5,-1,-1):
    if N - (5*i) == 0:
        cnt = i
        break
    else:
        if (N - (5*i)) % 3 == 0:
            cnt = i + ((N - (5*i)) // 3)
            break 

if cnt == 0:
    print(-1)
else:
    print(cnt)
