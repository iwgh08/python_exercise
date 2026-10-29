"""Day 4 · 문제 4 (보통) — 로그 한 줄에서 숫자 더하기"""


def sum_log_digits(line):
    """로그 문자열 line 에서 숫자 글자(0~9) 각각을 더한 값을 반환한다.

    규칙
    1. 숫자가 아닌 글자는 건너뛴다 (continue)
    2. '#' 을 만나면 그 뒤는 주석이므로 거기서 끝낸다 (break)

    >>> sum_log_digits("a1b2c3")
    6
    >>> sum_log_digits("loss=0.25#epoch9")
    7
    >>> sum_log_digits("#123")
    0
    """
    # TODO
    pass


if __name__ == "__main__":
    print(sum_log_digits("a1b2c3"))             # 6
    print(sum_log_digits("loss=0.25#epoch9"))   # 7
    print(sum_log_digits("epoch 10"))           # 1
    print(sum_log_digits("no digits"))          # 0
