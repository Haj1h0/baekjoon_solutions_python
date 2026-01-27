# 높은 자리수에 해당하는 알파벳에 큰 수를 배정한다. 
# 높은 자리수가 중복인 경우 그 이후 자릿수에서 더 최근에 나오는 알파벳을 선택한다. (가중치)
# 더 최근에 나오는 알파벳 또한 동일한 경우 결과는 동일하기에 순차적으로 수를 배정한다.

# ABCDE
# BACDE
# ABCDE
# BAADE

# ACCDE
# BDCDE
# ADADE
# BCADE

import sys

input = sys.stdin.readline

def main():

    m = 0
  
    A = [input().rstrip() for _ in range(int(input()))]    # 각 문자열 끝에 \n 존재 -> set("".join(A))에 '\n'도 포함
    al_dict = {char : 0 for char in set("".join(A))}    # 등장하는 알파벳을 키로 벨류는 0인 dict 생성

    # 각 자리마다 가중치 부여
    for i in A:
        for index, j in enumerate(i):
            al_dict[j] += 10**(len(i) - index -1)

    al = dict(sorted(al_dict.items(), key=lambda x: x[1], reverse=True))    # Value 기준 내림차순 (20, 10, 5 순) 만들고 다시 dict로
    
    for index, i in enumerate(al):
        al[i] = str(9 - index)

    for i in A:
        num_str = ''.join(al[ch] for ch in i)    # 새로운 문자열 생성
        m += int(num_str)
    
    return m
      
if __name__ == "__main__":
    print(main())
