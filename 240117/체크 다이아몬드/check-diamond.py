def print_check_diamond(n):
    for i in range(n):
        # 공백 출력
        print(' ' * (n - i - 1), end='')

        # 왼쪽 별표 출력
        print('* ', end='')

        # 오른쪽 별표 출력
        if i > 0:
            print('* ' * i, end='')

        print()

    for i in range(n - 2, -1, -1):
        # 공백 출력
        print(' ' * (n - i - 1), end='')

        # 왼쪽 별표 출력
        print('* ', end='')

        # 오른쪽 별표 출력
        if i > 0:
            print('* ' * i, end='')

        print()

# 입력 받기
n = int(input())

# 함수 호출
print_check_diamond(n)