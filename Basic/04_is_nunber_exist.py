# array 안에 숫자가 존재 하냐 안하냐 찾는 방법

input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    # array 하나하나를 element 으로 지정
    for element in array:
        # element 가 number랑 같으면 true
        if number == element:
            return True
    # 아니면 false
    return False


result = is_number_exist(3, input)
print(result)
