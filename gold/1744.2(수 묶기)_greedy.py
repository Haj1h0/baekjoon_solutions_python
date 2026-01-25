import sys

input = sys.stdin.readline

def main():
    sequence_p, sequence_n = [], []
    answer = 0
    has_zero = False
    
    n = int(input())
    for _ in range(n): 
        val = int(input())
        if val == 1:
            answer += 1 # 1은 무조건 더하기
        elif val == 0:
            has_zero = True
        elif val > 1:
            sequence_p.append(val)
        else:
            sequence_n.append(val)

    # 양수: 오름차순 정렬 (큰 수부터 pop)
    sequence_p.sort()
    while len(sequence_p) > 1:
        answer += sequence_p.pop() * sequence_p.pop()
    if sequence_p:
        answer += sequence_p.pop()

    # 음수: 내림차순 정렬 (절댓값 큰 수부터 pop)
    # 예: [-5, -3, -1] -> sort(reverse=True) -> [-1, -3, -5]
    # 뒤에서부터 pop하면 -5, -3 순서로 나옴
    sequence_n.sort(reverse=True)
    while len(sequence_n) > 1:
        answer += sequence_n.pop() * sequence_n.pop()
    
    # 남은 음수가 있고 0이 없다면 더함
    if sequence_n and not has_zero:
        answer += sequence_n.pop()
        
    return answer

if __name__ == "__main__":
    print(main())
