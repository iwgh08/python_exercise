"""Day 4 · 문제 1 (쉬움) — 1부터 N까지의 합"""


def sum_to_n(n):
    """1 + 2 + ... + n 을 반복문으로 계산해 반환한다. n 이 0 이하이면 0.

    >>> sum_to_n(5)
    15
    >>> sum_to_n(0)
    0
    """
    # TODO
    pass


if __name__ == "__main__":
    print(sum_to_n(5))     # 15
    print(sum_to_n(100))   # 5050
    print(sum_to_n(-3))    # 0
