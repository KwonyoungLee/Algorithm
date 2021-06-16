# 최댓값 찾기
# array 에서 가장 큰 수를 찾아 반환 하는 방법


input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    # array 하나하나를 num 으로 지정
    for num in array:
        # array 하나하나를 compare_num 으로 지정
        for compare_num in array:
            # 만약 num 이 compare_num 보다 작으면 실패. 더이상 실행 하지 않음
            if num < compare_num:
                break
        # 한번도 break 가 실행되지 않았다면 else (즉 그 값이 가장 큰 값)
        else:
            return num


result = find_max_num(input)
print(result)
