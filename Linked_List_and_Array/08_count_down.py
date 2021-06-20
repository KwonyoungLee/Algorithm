# 재귀함수란? 코드 안에 자기 자신을 부르는 코드가 존재함
# 반듯이 탈출 코드가 있어야 한다.
def count_down(number):
    if number < 0:
        return
    print(number)  # number를 출력하고
    count_down(number - 1)  # count_down 함수를 number - 1 인자를 주고 다시 호출한다!


count_down(60)
