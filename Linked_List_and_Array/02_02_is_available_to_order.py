shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


# set 집합을 이용 => 중복되는 숫자를 없애줌
# O(N) + O(M) = O(N+M)
# 이분탐색이 항상 효율적인게 아니다.

def is_available_to_order(menus, orders):
    menus_set = set(menus)  # O(N)
    for order in orders:  # M
        if order not in menus_set:  # O(1)
            return False

    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)