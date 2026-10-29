"""Day 3 · 문제 2 (쉬움) — 점수를 학점으로"""


def score_to_grade(score):
    """점수(int 또는 float)를 학점 문자열로 바꿔 반환한다.

    - 0 미만 또는 100 초과: "invalid"
    - 90 이상 "A", 80 이상 "B", 70 이상 "C", 60 이상 "D", 그 외 "F"

    >>> score_to_grade(95)
    'A'
    >>> score_to_grade(89.9)
    'B'
    >>> score_to_grade(101)
    'invalid'
    """
    if score > 100:
        return "invalid"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    elif score >= 0:
        return "F"
    else:
        return "invalid"


if __name__ == "__main__":
    print(score_to_grade(95))     # A
    print(score_to_grade(89.9))   # B
    print(score_to_grade(60))     # D
    print(score_to_grade(-1))     # invalid
