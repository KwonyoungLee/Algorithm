finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# 1번 탐색하면 반절 N/2
# 2번 탐색하면 반절 N/4 = N/2^2
# 3번 탐색하면 반절 N/8 = N/2^3
# k번 탐색하면 N/2^k => log2_N
# O(logN) (연산량이 반이 나눠진다 하면 보통 O(logN))

# 최솟값 = 1, 최댓값 = 16, 시돗값 = 8   => 8보다 큼
# 최솟값 = 9, 최댓값 = 16, 시돗값 = 12  => 12보다 큼
# 최솟값 = 13, 최댓값 = 16, 시돗값 = 14 => 찾음!

def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2
    find_count = 0
    while current_min <= current_max :
        find_count += 1
        if array[current_guess] == target:
            print(find_count)
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_max + current_min) // 2
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)
