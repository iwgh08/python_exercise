"""Day 4 · 문제 5 (도전) — 경사하강법은 몇 번 만에 수렴할까?

파라미터 w 하나짜리 모델, 손실 함수 loss = (w - 3) ** 2 (정답 w = 3).
매 step 마다  grad = 2 * (w - 3),  w = w - lr * grad  로 w 를 고친다.
"""


def steps_to_converge(w, lr, tol=0.01, max_steps=1000):
    """처음으로 loss < tol 이 될 때까지 필요한 업데이트 횟수를 반환한다.

    규칙
    1. 업데이트 전에 이미 loss < tol 이면 0
    2. 업데이트를 max_steps 번 한 뒤의 loss 까지 검사해도 tol 이상이면 -1

    >>> steps_to_converge(0, 0.5)
    1
    >>> steps_to_converge(3, 0.1)
    0
    >>> steps_to_converge(0, 1.1)
    -1
    """
    # TODO
    pass


if __name__ == "__main__":
    print(steps_to_converge(0, 0.1))                  # 16
    print(steps_to_converge(10, 0.05))                # 41
    print(steps_to_converge(0, 1.0))                  # -1
    print(steps_to_converge(0, 0.1, max_steps=16))    # 16
    print(steps_to_converge(0, 0.1, max_steps=15))    # -1
