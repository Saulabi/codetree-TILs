cnt = 0
sati = False

for i in range(5):
    num = int(input())
    if num % 3 == 0:
        cnt += 1

if cnt == 5:
    sati = True

if sati == False:
    print('0')
else:
    print('1')