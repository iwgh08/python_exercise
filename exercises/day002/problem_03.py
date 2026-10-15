"""Day 2 · 문제 3 (보통) — BMI 계산기"""


def bmi_report(weight_text, height_cm_text):
    """input()으로 받은 몸무게(kg)와 키(cm) 문자열로 BMI 요약 문자열을 반환한다.

    - BMI = 몸무게(kg) / 키(m)의 제곱   ← 키가 cm 로 들어온다는 점에 주의!
    - 입력은 "70", "175.5" 처럼 정수 또는 소수 형태의 문자열이다.

    형식: "키 <키:소수1자리>cm, 몸무게 <몸무게:소수1자리>kg → BMI <BMI:소수2자리>"

    >>> bmi_report("70", "175")
    '키 175.0cm, 몸무게 70.0kg → BMI 22.86'
    """
    # TODO
    return f'키 {float(height_cm_text):.1f}cm, 몸무게 {float(weight_text):.1f}kg → BMI {float(weight_text)/(float(height_cm_text)*0.01)**2:.2f}'


if __name__ == "__main__":
    print(bmi_report("70", "175"))      # 키 175.0cm, 몸무게 70.0kg → BMI 22.86
    weight = input("몸무게(kg): ")      # 직접 입력해 보세요
    height = input("키(cm): ")
    print(bmi_report(weight, height))
