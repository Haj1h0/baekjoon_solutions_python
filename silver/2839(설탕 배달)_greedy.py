import sys

input = sys.stdin.readline

def main():
    
    N = int(input())

    val = 0

    while (N - (3 * val)) % 5 != 0:
        val += 1
        if (N - (3 * val)) < 0:
            return -1
    
    return (N - (3 * val)) // 5 + val

if __name__ == "__main__":
    print(main())
