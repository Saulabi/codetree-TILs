sati = True

for _ in range(5):
    num = int(input())
    if num % 3 != 0:
        sati = False

if sati == True:
    print('1')
else:
    print('0')