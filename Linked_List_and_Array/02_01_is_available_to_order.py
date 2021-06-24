shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


# O(N * logN) + O(M * logN)
# O((M+N) * logN)
# 효율적이지 않음
def is_available_to_order(menus, orders):
    # shop_menus 를 정렬 해준다.
    # 정렬의 시간 복잡도는 O(배열의 길이 N * logN)
    shop_menus.sort()
    # shop_orders 에 있는 값들을 돌린다.
    # O(shop_orders의 길이 M * logN)
    for order in orders:
        # 만약 그 값이 shop_menus 안에 없으면 False 반환
        # 이분탐색의 시간 복잡도는 O(logN)
        if not is_existing_target_number_binary(order, menus):
            return False
    # 다 있으면 True
    return True


def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2
    while current_min <= current_max :
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_max + current_min) // 2
    return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)