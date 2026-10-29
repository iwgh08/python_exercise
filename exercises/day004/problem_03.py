"""Day 4 · 문제 3 (보통) — 소수 판별"""


def is_prime(n):
    """n 이 소수이면 True, 아니면 False 를 반환한다.

    - 소수: 1과 자기 자신으로만 나누어떨어지는 2 이상의 정수
    - 2 미만(1, 0, 음수)은 소수가 아니다

    >>> is_prime(2)
    True
    >>> is_prime(9)
    False
    >>> is_prime(1)
    False
    """
    # TODO
    pass


if __name__ == "__main__":
    print(is_prime(2), is_prime(9), is_prime(29))   # True False True
    print(is_prime(1), is_prime(-7))                # False False
    print(is_prime(1000003))                        # True
