# 주어진 수열을 정렬한 후, 음수는 작은 순서대로 두개씩 묶은 후 곱하고 양수는 큰 순서대로 두개씩 묶은 후 곱해서 더한다.
# 음수가 짝수개라면 0은 그대로 더하고, 음수가 홀수개라면 마지막 남은 음수에 0을 곱해 0으로 처리한다.
# 양수가 홀수개라면 마지막 남은 양수는 그대로 더한다.
# 1과는 곱하는 것보다 더하는 것이 더 크므로 1이 등장할 경우 더해서 처리한다.
 
import sys

input = sys.stdin.readline

def main():
    
    sequence_p, sequence_n = [], []
    answer, heck_zero = 0, 1
    
    for _ in range(int(input())): 
        val = int(input())
        if val == 1:
            answer += 1
            continue
        if val == 0:
            check_zero = 0
            continue
        if val > 0:
            sequence_p.append(val)
        else:
            sequence_n.append(val)

    sequence_p.sort()
    sequence_n.sort(reverse=True)

    while(len(sequence_p) > 1):
        a = sequence_p.pop()
        b = sequence_p.pop()  
        answer += a * b

    while(len(sequence_n) > 1):
        a = sequence_n.pop()
        b = sequence_n.pop()
        answer += a * b
        
    return answer + sum(sequence_n) * check_zero + sum(sequence_p) 

if __name__ == "__main__":
    print(main())        
