input = 80


# 소수는 자기 자신과 1 외 에는 아무것도 나눌 수 없다.
# 주어진 자연수 N이 소수이기 위한 필요 충분 조건은
# N이 N의 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않는다.
# 수가 수를 나누면 몫이 발생하는데, 몫과 나누는 수 둘 중 하나는
# 반드시 N의 제곱근 이하입니다.
# 그러면 수가 20 이였을때 2 - 20까지의 숫자를
# 2하고 3을 나눴을때의 경우만 체크해 주면 된다.
# 이렇게 까지 생각하려면 진짜 소수의 정의에 대해서 완벽히 이해 해야 할 것 같다.
def find_prime_list_under_number(number):
    # 초기값 설정
    prime_list = []

    # (2 - 20까지의)숫자를 나누기 위해 range를 설정합니다.
    array = range(2, number + 1)

    # (2 - 20 까지의)숫자들을 하나하나 num 으로 지정합니다.
    for num in array:
        i = 0
        while len(prime_list) > i and prime_list[i] * prime_list[i] <= num:
            if num % prime_list[i] == 0:
                break
            i += 1
        else:
            prime_list.append(num)
    return prime_list


result = find_prime_list_under_number(input)
print(result)
