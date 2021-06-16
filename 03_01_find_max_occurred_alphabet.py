# 최빈값 찾기
# 그러기 위해선
# 알파벳의 빈도수를 세는 방법
# 그리고 제일 많이 쓰여진 알파벳을 찾는 방법

input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                      "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    # 초기값 설정
    max_occurrence = 0
    max_alphabet = alphabet_array[0]

    # alphabet_array 하나하나를 alphabet 으로 지정
    for alphabet in alphabet_array:
        occurrence = 0
        # string 하나하나를 char 으로 지정
        for char in string:
            # char 이랑 alphabet이 같다면 +1
            if char == alphabet:
                occurrence += 1

        if occurrence > max_occurrence:
            max_occurrence = occurrence
            max_alphabet = alphabet
    return max_alphabet


result = find_max_occurred_alphabet(input)
print(result)
