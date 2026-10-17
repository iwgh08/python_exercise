"""Day 3 · 문제 4 (보통) — 예측 확률에 확신도 붙이기"""


def confidence_label(prob_text):
    """문자열로 받은 positive 확률로 "<라벨> (<확신도>)" 문자열을 반환한다.

    1. 확률이 0 미만이거나 1 초과면 "invalid"
    2. 라벨: 0.5 이상이면 "positive", 아니면 "negative"
    3. 확신도:
       - 0.9 이상이거나 0.1 이하  → "high"
       - 0.4 초과 0.6 미만        → "low"
       - 그 외                    → "medium"

    >>> confidence_label("0.97")
    'positive (high)'
    >>> confidence_label("0.5")
    'positive (low)'
    >>> confidence_label("1.2")
    'invalid'
    """
    # TODO
    pass


if __name__ == "__main__":
    print(confidence_label("0.97"))   # positive (high)
    print(confidence_label("0.03"))   # negative (high)
    print(confidence_label("0.75"))   # positive (medium)
    print(confidence_label("0.4"))    # negative (medium)
    print(confidence_label("1.2"))    # invalid
