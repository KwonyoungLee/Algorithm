input = "abcba"

#abcba
#bcb
#c

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