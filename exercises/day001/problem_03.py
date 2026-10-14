"""Day 1 · 문제 3 (보통) — 모델 학습 소요 시간 표시하기"""


def seconds_to_hms(total_seconds):
    """학습에 걸린 총 시간(초, 0 이상의 정수)을 "H시간 M분 S초" 문자열로 반환한다.

    - 0인 단위도 생략하지 않고 그대로 표시한다.

    >>> seconds_to_hms(3725)
    '1시간 2분 5초'
    >>> seconds_to_hms(59)
    '0시간 0분 59초'
    """
    # TODO: // 와 % 를 사용해 hours, minutes, seconds 를 구한 뒤 문자열로 조립하세요.
    return print(str(total_seconds // 3600)+'시간 '+str((total_seconds % 3600)//60)+'분 '+str((total_seconds % 3600)%60)+'초')


if __name__ == "__main__":
    print(seconds_to_hms(3725))   # 1시간 2분 5초
    print(seconds_to_hms(86399))  # 23시간 59분 59초
