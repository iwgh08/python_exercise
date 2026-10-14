"""Day 1 · 문제 5 (도전) — 데이터로더 요약 문자열 만들기

PyTorch의 DataLoader는 데이터를 배치로 나눌 때 "배치가 몇 개인지, 마지막 배치는 몇 개인지"가
중요합니다. 이 정보를 한 줄로 요약하는 함수를 만들어 봅시다.
"""


def batch_summary(n_samples, batch_size):
    """배치 분할 정보를 요약한 문자열을 반환한다. (n_samples, batch_size 는 1 이상의 정수)

    형식: "샘플 <n_samples>개 / 배치 크기 <batch_size> → 배치 <배치 개수>개, 마지막 배치 <마지막 배치 크기>개"

    - 나누어떨어지면 마지막 배치 크기는 batch_size 와 같다.
    - 조건문(if) 없이 산술 연산만으로 해결하세요.
    - 문제 4의 아이디어를 재사용해도 됩니다.

    >>> batch_summary(1000, 32)
    '샘플 1000개 / 배치 크기 32 → 배치 32개, 마지막 배치 8개'
    >>> batch_summary(64, 32)
    '샘플 64개 / 배치 크기 32 → 배치 2개, 마지막 배치 32개'
    """
    # TODO
    pass


if __name__ == "__main__":
    print(batch_summary(1000, 32))
    print(batch_summary(64, 32))
    print(batch_summary(5, 10))
