# 최빈값 찾기
# 그러기 위해선
# 알파벳의 빈도수를 세는 방법

def find_alphabet_occurrence_array(string):
    # 초기 array 설정
    alphabet_occurrence_array = [0] * 26

    # string 하나하나를 char 으로 지정
    for char in string:
        # char 이 알파벳이 아니라면 continue 맞다면 다음 코드라인 실행
        if not char.isalpha():
            continue
        # ASCII 코드 이용하기 (ord함수 사용으로 ASCII코드 10진법 숫자로 변환)
        arr_index = ord(char) - ord("a") #소문자만 쓴다는 전제하에 가능함
        alphabet_occurrence_array[arr_index] += 1

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))