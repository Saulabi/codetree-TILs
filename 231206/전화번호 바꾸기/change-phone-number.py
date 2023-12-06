pb = input()

sn = pb.split('-')

sn[1], sn[2] = sn[2], sn[1]

result = '-'.join(sn)
print(result)