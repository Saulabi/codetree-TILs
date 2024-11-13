n = int(input())  # 정수 n 입력받기

# 1부터 n까지의 홀수 출력
for i in range(1, n + 1, 2):  # 1부터 n까지 2씩 증가하며 홀수만 처리
    print(i, end=" ")  # 공백을 사이에 두고 출력