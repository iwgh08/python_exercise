"""Day 4 · 문제 2 (쉬움) — 특정 문자 개수 세기"""


def count_char(text, target):
    """text 안에 target(한 글자)이 몇 번 나오는지 반환한다. 대소문자 구분.

    str.count() 를 쓰지 말고 반복문으로 직접 센다.

    >>> count_char("banana", "a")
    3
    >>> count_char("", "a")
    0
    """
    # TODO
    pass


if __name__ == "__main__":
    print(count_char("banana", "a"))          # 3
    print(count_char("Deep Learning", "e"))   # 3
    print(count_char("hello world", " "))     # 1
