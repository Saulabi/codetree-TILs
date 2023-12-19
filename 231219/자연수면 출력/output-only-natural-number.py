a, b = map(int, input().split())

i = 0
while i < b:
    if a > 0:
        print(a, end='')
        i += 1
    else:
        print('0')