"""Day 2 · 문제 2 (쉬움) — 모델 정확도 표시"""


def format_accuracy(correct, total):
    """맞힌 개수(correct)와 전체 개수(total)로 정확도 문자열을 만들어 반환한다. (total ≥ 1)

    형식: "정확도: XX.XX%"  (퍼센트, 소수점 둘째 자리)

    >>> format_accuracy(875, 1000)
    '정확도: 87.50%'
    >>> format_accuracy(1, 3)
    '정확도: 33.33%'
    """
    # TODO: f-string 을 사용하세요.
    pass


if __name__ == "__main__":
    print(format_accuracy(875, 1000))  # 정확도: 87.50%
    print(format_accuracy(2, 3))       # 정확도: 66.67%
