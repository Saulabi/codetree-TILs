# 초기값 설정
total_age = 0
count = 0

# 입력 받기
while True:
    age = int(input())
    
    # 20대가 아닌 다른 나이대가 입력되면 루프 종료
    if age < 20 or age >= 30:
        break
    
    # 입력된 나이 더하기
    total_age += age
    count += 1

# 평균 계산 및 출력
average = total_age / count
print(f"{average:.2f}")