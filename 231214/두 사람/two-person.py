p1 = input().split()
p2 = input().split()

if (int(p1[0]) >= 19) or (int(p2[0]) >= 19):
    if (p1[1]== 'M') or (p2[1] == 'M'):
        print('1')
    else:
        print('0')
else:
    print('0')