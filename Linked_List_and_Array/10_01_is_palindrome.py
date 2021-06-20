input = "abcba"


def is_palindrome(string):
    # input 의 길이
    n = len(string)
    for i in range(n):
        if string[i] != string[n - 1 - i]:
            return False
    return True

print(is_palindrome(input))