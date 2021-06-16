# 'X' '+' 이용하여 가장 큰 값의 결과 반환 하는 방법

input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    # 초기값 설정
    multiply_sum = 0

    # number 가 0 이나 1이거나 계산한 값이 0 이나 1이면
    # 곱화는 것보다 더하는 것이 더 큰 수가 나온다.
    for number in array:
        if number <= 1 or multiply_sum <= 1:
            multiply_sum += number
        else:
            multiply_sum *= number
    return multiply_sum


result = find_max_plus_or_multiply(input)
print(result)