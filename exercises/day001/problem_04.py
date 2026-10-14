"""Day 1 · 문제 4 (보통) — 미니배치 개수 구하기"""


def count_batches(n_samples, batch_size):
    """샘플 n_samples개(1 이상)를 batch_size개(1 이상)씩 나눌 때 필요한 배치 개수를 반환한다.

    - 마지막 배치는 batch_size보다 작아도 하나의 배치로 센다.
    - 조건문(if)은 아직 배우지 않았으므로 **산술 연산만으로** 해결하세요.

    >>> count_batches(1000, 32)   # 꽉 찬 배치 31개 + 8개짜리 배치 1개
    32
    >>> count_batches(64, 32)     # 딱 나누어떨어짐
    2
    """
    # TODO
    return (n_samples + batch_size - 1)//batch_size


if __name__ == "__main__":
    print(count_batches(1000, 32))  # 32
    print(count_batches(64, 32))    # 2
    print(count_batches(5, 10))     # 1
