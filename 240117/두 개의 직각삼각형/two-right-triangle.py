def print_symmetric_triangle(n):
    for i in range(n, 0, -1):
        # 왼쪽 별표 출력
        print('*' * i, end='')

        # 중간 공백 출력
        spaces = 2 * (n - i)
        if spaces > 0:
            print(' ' * spaces, end='')

        # 오른쪽 별표 출력
        print('*' * i)

# 입력 받기
n = int(input())

# 함수 호출
print_symmetric_triangle(n)