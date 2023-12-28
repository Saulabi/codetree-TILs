def solution(n):
    mlp = 1
    num = 1
    while True:
        num += 1
        mlp *= num
        if mlp >= n:
            break

    return num

n = int(input())

print(solution(n))