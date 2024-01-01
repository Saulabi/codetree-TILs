def solution(n):
    cnt = 0
    divisor = 1
    
    while True:
        cnt += 1
        n //= divisor
        divisor += 1

        if n <= 1:
            break

    return cnt

n = int(input())

print(solution(n))