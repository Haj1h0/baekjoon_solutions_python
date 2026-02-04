import sys
from itertools import combinations

input = sys.stdin.readline

def main():
    
    L, C = map(int,input().split())
    ch = list(input().split())
    vowel = "aeiou"

    # 정렬된 ch에서 길이가 L이 되도록 (len(ch) - L)개 만큼의 원소를 제거 후 최소 한 개의 모음, 최소 두 개의 자음으로 구성되어 있는지 조건을 확인한다.
    # 조건이 충족된다면 해당 문자열을 출력한다.
    # 중복되지 않도록 원소를 제거하는 것을 반복한다.
    
    ch.sort()
    index = [i for i in range(len(ch))]
    combi = combinations(index, L)
    # ((0,1,3,5),(0,1,4,5)...)
    for i in combi:
        a, b = 1, 2    # 모음a, 자음b
        ans = []
        for j in i:
            ans.append(ch[j])
            if ch[j] in vowel:
                a -= 1
            else:
                b -= 1
        if a <= 0 and b <= 0:
            print(''.join(ans))    # a와 b가 둘중에 하나라도 양수이면 실행 x
        
if __name__ == '__main__':
    main()
