"""Day 3 · 문제 1 (쉬움) — 예측 확률을 라벨로 바꾸기"""


def label_prediction(prob, threshold):
    """이진 분류 모델의 positive 확률(prob)을 라벨 문자열로 바꿔 반환한다.

    - prob 가 threshold 이상이면 "positive", 아니면 "negative"

    >>> label_prediction(0.7, 0.5)
    'positive'
    >>> label_prediction(0.49, 0.5)
    'negative'
    """
    # TODO
    if prob >= threshold:
        return "positive"
    else:
        return "negative"


if __name__ == "__main__":
    print(label_prediction(0.7, 0.5))    # positive
    print(label_prediction(0.5, 0.5))    # positive
    print(label_prediction(0.85, 0.9))   # negative
