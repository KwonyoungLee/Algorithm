# 최빈값 찾기
# 그러기 위해선
# 알파벳의 빈도수를 세는 방법
# 그리고 제일 많이 쓰여진 알파벳을 찾는 방법

def find_max_occurred_alphabet(string):
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

    # 초기값 설정
    max_occurrence = 0
    max_alphabet_index = 0
    # range(len) : 어떠한 array의 길이를 0 부터 길이까지 지정 -> 0 - 25(=길이 26)
    for index in range(len(alphabet_occurrence_array)):
        # index 0 -> alphabet_occurrence 3
        alphabet_occurrence = alphabet_occurrence_array[index]
        # 가장 많이 카운트 된 (높은) array index 를 max_alphabet_index로 지정
        # 그리구 얼마나 카운트 됬는지 그 수를 max_occurrence에 지정
        if alphabet_occurrence > max_occurrence:
            max_alphabet_index = index
            max_occurrence = alphabet_occurrence_array[index]
    # chr : ascii 코드를 이용하여 알파벳으로 변환
    # ord("a") = 97
    return chr(max_alphabet_index + ord("a"))


result = find_max_occurred_alphabet("hello my name is sparta")
print(result)
