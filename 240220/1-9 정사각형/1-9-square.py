n = int(input())

for i in range(1, n*n+1):
    print((i - 1) % 9 + 1, end='')
    if i % n == 0:
        print()