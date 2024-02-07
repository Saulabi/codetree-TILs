n = int(input())

for i in range(n, 0, -1):
    for j in range(n, 0, -1):
        print(f'({i},{j})', end=' ')
    print()


# # 변수 선언 및 입력
# n = int(input())
	
# # n칸의 정사각형에 올바른 순서쌍을 출력합니다.
# for i in range(n):
# 	for j in range(n):
# 		print(f"({n - i},{n - j})", end=" ")
# 	print()