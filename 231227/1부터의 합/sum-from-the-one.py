def solution(n):

    total = 0
    num = 0

    while True:
        num += 1
        total += num

        if total >= n:
            break

    return num

n = int(input())

print(solution(n))