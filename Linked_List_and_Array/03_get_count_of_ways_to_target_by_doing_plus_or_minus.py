numbers = [1, 1, 1, 1, 1]
target_number = 3

# N 의 길이의 배열에서 더하거나 뺀 모든 경우의 수는
# N-1 의 길이의 배열에서 마지막 원소를 더하거나 뺀 경우의 수를
# 추가하면 됨.


result_count = 0


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index, current_sum):
    if current_index == len(numbers):
        if current_sum == target:
            global result_count
            result_count += 1
        return
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1,
                                                       current_sum + numbers[current_index])
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1,
                                                       current_sum - numbers[current_index])


get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, 0)
print(result_count)
