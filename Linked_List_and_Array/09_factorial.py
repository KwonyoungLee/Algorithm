# 5 * 4 * 3 * 2 * 1
# 재귀 함수에는 항상 탈출 코드가 필요함

def factorial(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n * factorial(n-1)


print(factorial(5))