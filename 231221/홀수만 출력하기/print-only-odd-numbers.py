n = int(input())

for _ in range(n):
    num = int(input())
    if (num % 2 != 0) and (num % 3) == 0:
        print(num)