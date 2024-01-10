for i in range(5):
    num = int(input())
    cnt = 0
    sati = False
    if num % 3 == 0:
        cnt += 1

if cnt == 5:
    sati = True

if sati == False:
    print('1')
else:
    print('0')