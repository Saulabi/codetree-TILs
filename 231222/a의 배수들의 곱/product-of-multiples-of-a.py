a, b = map(int, input().split())

_prod = 1
for i in range(1, b+1):
    if i % a == 0:
        _prod *= i

print(_prod)