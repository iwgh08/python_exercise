# Day 2 문제 · 연산자, 형 변환, input, f-string

개념 설명: [docs/day002.md](../../docs/day002.md)

각 `problem_XX.py`의 `# TODO`를 채우고 `pass`를 지우세요. **`print`가 아니라 `return`!**

```powershell
pytest exercises/day002 -v
python exercises/day002/problem_03.py   # 3번은 input() 으로 직접 입력도 해 볼 수 있어요
```

다 풀면 "채점해줘"라고 말해 주세요.

| # | 난이도 | 함수 | 핵심 개념 |
| --- | --- | --- | --- |
| 1 | 쉬움 | `total_score(a, b, c)` | `int()` 변환 |
| 2 | 쉬움 | `format_accuracy(correct, total)` | f-string `%` 포맷 |
| 3 | 보통 | `bmi_report(weight_text, height_cm_text)` | `float()`, 단위 변환, `**`, `.Nf` |
| 4 | 보통 | `is_close(pred_text, target, tol)` | 부동소수점 비교, 비교 연산자 → bool |
| 5 | 도전 | `format_log(epoch_text, total_text, loss_text, acc_text)` | 변환 + 여러 포맷 + 자릿수 맞추기 |

---

## 문제 1 (쉬움) 문자열 점수 합계

| 입력 | 출력 |
| --- | --- |
| `"90", "85", "77"` | `252` |
| `"-5", "10", "3"` | `8` |

## 문제 2 (쉬움) 정확도 표시

| 입력 | 출력 |
| --- | --- |
| `875, 1000` | `"정확도: 87.50%"` |
| `2, 3` | `"정확도: 66.67%"` |
| `10, 10` | `"정확도: 100.00%"` |

## 문제 3 (보통) BMI 계산기

키는 **cm**로 들어오지만 공식은 **m**를 씁니다.

| 입력 | 출력 |
| --- | --- |
| `"70", "175"` | `"키 175.0cm, 몸무게 70.0kg → BMI 22.86"` |
| `"55.5", "162.3"` | `"키 162.3cm, 몸무게 55.5kg → BMI 21.07"` |

## 문제 4 (보통) 거의 같은지 판별

`0.1 + 0.2 == 0.3`이 False인 문제를 해결하는 함수입니다. **if 없이** 한 줄로 가능합니다.

| 입력 | 출력 |
| --- | --- |
| `"0.30000000000000004", 0.3, 1e-9` | `True` |
| `"0.31", 0.3, 0.001` | `False` |
| `"0.29", 0.3, 0.02` | `True` |

## 문제 5 (도전) 학습 로그 한 줄

| 입력 | 출력 |
| --- | --- |
| `"3", "10", "0.123456", "0.925"` | `"Epoch 03/10 \| loss 0.1235 \| acc 92.5%"` |
| `"7", "100", "2.5", "0.1"` | `"Epoch 007/100 \| loss 2.5000 \| acc 10.0%"` |
| `"1", "5", "1.23456789", "0.33333"` | `"Epoch 1/5 \| loss 1.2346 \| acc 33.3%"` |
| `"42", "1000", "0.05", "0.8771"` | `"Epoch 0042/1000 \| loss 0.0500 \| acc 87.7%"` |

epoch의 자릿수가 **total의 자릿수에 따라 달라진다**는 점이 핵심입니다.

---

## 힌트 (막혔을 때만 펼쳐 보세요)

<details>
<summary>문제 1 힌트</summary>

`int(a) + int(b) + int(c)`
</details>

<details>
<summary>문제 2 힌트</summary>

`correct / total`은 0~1 사이 값입니다. `:.2%` 포맷은 알아서 ×100 하고 `%`를 붙여 줍니다. 직접 `* 100` 하고 `:.2f`에 `"%"`를 붙여도 됩니다.
</details>

<details>
<summary>문제 3 힌트</summary>

1. `weight = float(weight_text)`, `height_cm = float(height_cm_text)`
2. `height_m = height_cm / 100`
3. `bmi = weight / height_m ** 2` (`**`가 `/`보다 먼저 계산되므로 괄호 없어도 OK)
4. f-string에서 `:.1f`, `:.2f` 사용
</details>

<details>
<summary>문제 4 힌트</summary>

`abs(float(pred_text) - target) <= tol` 이라는 비교식 자체가 True/False 값입니다. 이걸 그대로 `return` 하면 됩니다.
</details>

<details>
<summary>문제 5 힌트 1 — 자릿수</summary>

total의 자릿수는 `len(total_text)`로 구할 수 있습니다 (`len("100")` → 3). total_text가 이미 문자열이라 편하죠.
</details>

<details>
<summary>문제 5 힌트 2 — 폭을 변수로</summary>

`f"{7:03d}"`에서 폭 `3` 자리에 `{}`를 넣을 수 있습니다: `width = 3` 이면 `f"{7:0{width}d}"` → `"007"`. 단, `d` 포맷을 쓰려면 epoch가 **int**여야 합니다.
</details>

<details>
<summary>문제 5 힌트 3 — 나머지</summary>

loss는 `float()` 후 `:.4f`, acc는 `float()` 후 `:.1%`.
</details>
