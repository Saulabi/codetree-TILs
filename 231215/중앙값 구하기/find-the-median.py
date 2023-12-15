a, b, c = map(int, input().split())

if (a < b < c) or (c < b < a):
    result = b
elif (b < a < c) or (c < a < b):
    result = a
else:
    result = c

print(result)