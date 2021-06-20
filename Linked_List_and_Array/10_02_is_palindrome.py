input = "abcba"

#abcba
#bcb
#c
# 재귀함수를 풀기 위해선 
# 문제가 축소되는 특징이 보여야 합니다.
# 특정 구조가 반복되는 것 같은 양상을 보였으면 재귀함수로 시도 가능.
def is_palindrome(string):
    # input 의 길이가 1이거나 작다면
    if len(string) <= 1:
        return True
    # input 의 첫번째와 끝번째가 같지 않다면
    if string[0] != string[-1]:
        return False
    # 재귀함수
    return is_palindrome(string[1:-1])


print(is_palindrome(input))