input = "abadabac"


def find_not_repeating_character(string):
    # 초기 array 설정
    alphabet_occurrence_array = [0] * 26

    # string 하나하나를 char 으로 지정
    for char in string:
        # char 이 알파벳이 아니라면 continue 맞다면 다음 코드라인 실행
        if not char.isalpha():
            continue
        # ASCII 코드 이용하기 (ord함수 사용으로 ASCII코드 10진법 숫자로 변환)
        arr_index = ord(char) - ord("a")  # 소문자만 쓴다는 전제하에 가능함
        alphabet_occurrence_array[arr_index] += 1

    # 초기값 설정 (array for not repeating alphabet)
    not_repeating_character_array = []
    # alphabet_occurrence_array 를 순서대로 스캔해서
    # 한번씩 밖에 사용되지 않은 문자들을 not_repeating_character_array 에
    # character 로 변환환서 넣어 준다.
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index + ord("a")))

    # 다시 원래 input을 스캔해서 not_repeating_character_array에 있는
    # character 바로 반환.
    # 없을 시 "_" 반환.
    for char in string:
        if char in not_repeating_character_array:
            return char
        else:
            return "_"


result = find_not_repeating_character(input)
print(result)
