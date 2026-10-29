"""Day 3 · 문제 3 (보통) — 윤년 판별"""


def is_leap_year(year):
    """year 가 윤년이면 True, 아니면 False 를 반환한다.

    - 4로 나누어떨어지면 윤년
    - 단, 100으로 나누어떨어지면 윤년이 아님
    - 단, 400으로 나누어떨어지면 윤년

    >>> is_leap_year(2024)
    True
    >>> is_leap_year(1900)
    False
    >>> is_leap_year(2000)
    True
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    else:
        return False


if __name__ == "__main__":
    for y in (2024, 2023, 1900, 2000):   # for 문은 내일 배웁니다. 지금은 확인용으로만!
        print(y, is_leap_year(y))
