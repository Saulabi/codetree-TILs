n = int(input())

if n % 2 == 1:
    for i in range(1, n+1):
        print('*'*(2*i-1))