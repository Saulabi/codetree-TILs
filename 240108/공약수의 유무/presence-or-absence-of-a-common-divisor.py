def find_common_divisor(a, b):
    # a 이상 b 이하의 수 중에서 1,920과 2,880의 공약수를 찾는 함수
    for i in range(a, b+1):
        if 1920 % i == 0 and 2880 % i == 0:
            return 1  # 공약수가 존재하는 경우
        else:
            return 0  # 공약수가 존재하지 않는 경우

# 입력 받기
a, b = map(int, input().split())

# 결과 출력
result = find_common_divisor(a, b)
print(result)