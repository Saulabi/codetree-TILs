a,b = map(int,input().split())

satisfied = False

for i in range(a, b + 1):
	# a에서 b사이의 값 중 공약수가 있는지 확인합니다.
	if 1920 % i == 0 and 2880 % i == 0:
		satisfied = True


# 출력
if satisfied == True:
	print("1")
else:
	print("0")