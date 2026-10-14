"""Day 1 · 문제 1 (쉬움) — 섭씨를 화씨로 변환하기"""


def celsius_to_fahrenheit(celsius):
    """섭씨 온도(celsius)를 화씨 온도로 바꿔 반환한다.

    공식: F = C × 9 / 5 + 32

    >>> celsius_to_fahrenheit(100)
    212.0
    """
    # TODO: 공식을 그대로 코드로 옮겨 return 하세요.
    return celsius * 9 / 5 + 32


if __name__ == "__main__":
    print(celsius_to_fahrenheit(0))     # 32.0
    print(celsius_to_fahrenheit(36.5))  # 97.7
