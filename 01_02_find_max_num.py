# 최댓값 찾기
# array 에서 가장 큰 수를 찾아 반환 하는 방법

input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    # 초기값 설정 (3)
    max_num = array[0]
    # array 하나하나를 num 으로 지정
    for num in array:
        # num 이 max_num 보다 크면 max_num을 그 num 값으로 지정
        # 같거나 작으면 그냥 아무것도 하지않고 그대로 둠
        if num > max_num:
            max_num = num

    return max_num


result = find_max_num(input)
print(result)
