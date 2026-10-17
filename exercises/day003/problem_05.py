"""Day 3 · 문제 5 (도전) — Early Stopping: 학습을 계속할까, 멈출까?

딥러닝은 매 epoch 이 끝날 때 검증 손실(val_loss)을 보고 다음 행동을 정합니다.
손실이 좋아지면 모델을 저장(save)하고, 한동안 좋아지지 않으면 과적합을 막기 위해 멈춥니다(stop).
"""


def training_decision(epoch, max_epochs, val_loss, best_loss, bad_epochs, patience):
    """이번 epoch 결과로 다음 행동을 "save" / "save, stop" / "stop" / "wait" 중 하나로 반환한다.

    - best_loss: 지금까지의 최저 손실. 첫 epoch 에는 기록이 없어 None 이다.
    - bad_epochs: 이번 epoch '전까지' 연속으로 개선되지 않은 epoch 수

    규칙
    1. 개선: best_loss 가 None 이거나 val_loss < best_loss  (같으면 개선 아님)
    2. 개선됨 → "save". 단, 마지막 epoch(epoch >= max_epochs)이면 "save, stop"
    3. 개선 안 됨 + 마지막 epoch → "stop"
    4. 개선 안 됨 + (bad_epochs + 1) >= patience → "stop"
    5. 그 외 → "wait"

    >>> training_decision(1, 10, 0.9, None, 0, 3)
    'save'
    >>> training_decision(5, 10, 0.6, 0.5, 2, 3)
    'stop'
    >>> training_decision(3, 10, 0.1, 0.0, 0, 3)
    'wait'
    """
    # TODO
    pass


if __name__ == "__main__":
    print(training_decision(1, 10, 0.9, None, 0, 3))   # save
    print(training_decision(5, 10, 0.5, 0.5, 0, 3))    # wait
    print(training_decision(5, 10, 0.6, 0.5, 2, 3))    # stop
    print(training_decision(10, 10, 0.3, 0.5, 0, 3))   # save, stop
    print(training_decision(3, 10, 0.1, 0.0, 0, 3))    # wait
