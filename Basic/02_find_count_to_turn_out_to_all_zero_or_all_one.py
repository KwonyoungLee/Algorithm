input = "111111"


# 1) 0에서 1 혹은 1에서 0으로 바뀔때
# 2) 첫번째 숫자가 0 인지 1인지에 따라서 count 추가
def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 초기값 설정
    count_zero = 0
    count_one = 0

    # 첫번째 숫자가 0인지 1인지 판단하기위해 설정
    initial_number = string[0]

    # 첫번째 숫자가 0 일때
    # 모두 1로 바뀌는 횟수 증가
    if initial_number == '0':
        count_one += 1
    # 첫번째 숫자가 1 일때
    # 모두 0로 바뀌는 횟수 증가
    elif initial_number == '1':
        count_zero += 1

    for num in range(len(string) - 1):
        # 1 에서 0 혹은 0 에서 1 로 바뀌었을때
        # 횟수 증가
        if string[num] != string[num + 1]:
            # 1에서 0 으로 바뀔 때
            # 모두 1로 바꾸기 위한 횟수 1 증가
            if string[num + 1] == '0':
                count_one += 1
            # 0에서 1으로 바뀔 때
            # 모두 0으로 바꾸기 위한 횟수 1 증가
            elif string[num + 1] == '1':
                count_zero += 1

    # 최소값 반환환
    return min(count_zero, count_one)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)

