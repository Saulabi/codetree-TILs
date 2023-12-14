p1 = input().split()
p2 = input().split()

print(int((int(p1[0]) >= 19 and p1[1] == 'M') or (int(p2[0]) >= 19 and p2[1] == 'M')))