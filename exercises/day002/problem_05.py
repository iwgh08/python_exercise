"""Day 2 · 문제 5 (도전) — 학습 로그 한 줄 만들기

딥러닝 학습 중에는 매 epoch 마다 이런 로그를 찍습니다.
    Epoch 003/100 | loss 0.1235 | acc 92.5%
설정 파일이나 명령줄에서 읽은 값은 문자열이므로, 변환과 포맷을 함께 다뤄야 합니다.
"""


def format_log(epoch_text, total_text, loss_text, acc_text):
    """문자열로 받은 학습 정보를 로그 한 줄로 만들어 반환한다.

    - epoch_text, total_text: 정수 문자열 (예: "3", "100")
    - loss_text: 손실값 문자열 (예: "0.123456") → 소수점 넷째 자리까지
    - acc_text: 정확도 문자열, 0~1 사이 (예: "0.925") → 퍼센트, 소수점 첫째 자리
    - **epoch 는 total 과 자릿수가 같도록 앞을 0으로 채운다.**
        total 이 "10"(2자리)이면 3 → "03", total 이 "100"(3자리)이면 3 → "003"

    형식: "Epoch <epoch>/<total> | loss <loss> | acc <acc>"

    >>> format_log("3", "10", "0.123456", "0.925")
    'Epoch 03/10 | loss 0.1235 | acc 92.5%'
    >>> format_log("7", "100", "2.5", "0.1")
    'Epoch 007/100 | loss 2.5000 | acc 10.0%'
    """
    # TODO
    return f"Epoch {int(epoch_text):0{len(total_text)}d}/{int(total_text)} | loss {float(loss_text):.4f} | acc {float(acc_text):.1%}"


if __name__ == "__main__":
    print(format_log("3", "10", "0.123456", "0.925"))
    print(format_log("7", "100", "2.5", "0.1"))
    print(format_log("1", "5", "1.23456789", "0.33333"))
