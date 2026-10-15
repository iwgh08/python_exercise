"""Day 2 · 문제 4 (보통) — 예측값이 정답과 '거의 같은지' 판별"""


def is_close(pred_text, target, tol):
    """모델이 문자열로 출력한 예측값(pred_text)이 정답(target, float)과 거의 같은지 판별한다.

    - 두 값의 차이의 절댓값이 tol 이하이면 True, 아니면 False 를 반환한다.
    - 조건문(if) 없이 비교 연산자만으로 해결하세요. (비교 연산의 결과 자체가 bool 입니다)
    - 힌트: 절댓값은 abs() 내장 함수로 구합니다. abs(-3) → 3

    >>> is_close("0.30000000000000004", 0.3, 1e-9)
    True
    >>> is_close("0.31", 0.3, 0.001)
    False
    """
    # TODO
    pass


if __name__ == "__main__":
    print(0.1 + 0.2 == 0.3)                          # False
    print(is_close(str(0.1 + 0.2), 0.3, 1e-9))       # True
    print(is_close("0.31", 0.3, 0.001))              # False
