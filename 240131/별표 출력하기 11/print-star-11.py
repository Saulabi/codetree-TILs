n = int(input())

for i in range(1, 2*n+2):
    for j in range(1, 2*n+2):
        if i % 2 == 0 and j % 2 == 0:
            print("  ", end='')
        else:
            print("* ", end='')
    print()