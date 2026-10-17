# Day 3 문제 · 조건문

개념 설명: [docs/day003.md](../../docs/day003.md)

각 `problem_XX.py`의 `# TODO`를 채우고 `pass`를 지우세요.

```powershell
.venv\Scripts\Activate.ps1
pytest exercises/day003 -v
```

다 풀면 "채점해줘"라고 말해 주세요.

| # | 난이도 | 함수 | 핵심 개념 |
| --- | --- | --- | --- |
| 1 | 쉬움 | `label_prediction(prob, threshold)` | if/else, 경계값 |
| 2 | 쉬움 | `score_to_grade(score)` | if/elif/else 순서 |
| 3 | 보통 | `is_leap_year(year)` | `and`/`or`/`not` 결합, `%` |
| 4 | 보통 | `confidence_label(prob_text)` | 형 변환 + 연쇄 비교 + f-string |
| 5 | 도전 | `training_decision(...)` | 조건 우선순위, `is None`, 단락 평가 |

---

## 문제 1 (쉬움) 예측 확률 → 라벨

이진 분류 모델이 "positive일 확률"을 출력합니다. 확률이 임계값(threshold) **이상**이면 `"positive"`, 아니면 `"negative"`를 반환하세요.

| 입력 | 출력 |
| --- | --- |
| `0.7, 0.5` | `"positive"` |
| `0.5, 0.5` | `"positive"` (같으면 positive) |
| `0.49, 0.5` | `"negative"` |
| `0.85, 0.9` | `"negative"` |

## 문제 2 (쉬움) 점수 → 학점

| 점수 | 학점 |
| --- | --- |
| 90 이상 | `"A"` |
| 80 이상 | `"B"` |
| 70 이상 | `"C"` |
| 60 이상 | `"D"` |
| 60 미만 | `"F"` |
| 0 미만 또는 100 초과 | `"invalid"` |

| 입력 | 출력 |
| --- | --- |
| `95` | `"A"` |
| `89.9` | `"B"` |
| `60` | `"D"` |
| `101` | `"invalid"` |

## 문제 3 (보통) 윤년 판별

- 4로 나누어떨어지면 윤년
- 단, 100으로 나누어떨어지면 윤년이 **아님**
- 단, 400으로 나누어떨어지면 다시 윤년

True/False를 반환합니다.

| 입력 | 출력 |
| --- | --- |
| `2024` | `True` |
| `2023` | `False` |
| `1900` | `False` |
| `2000` | `True` |

## 문제 4 (보통) 확신도 라벨

모델이 출력한 확률이 **문자열**로 들어옵니다. 다음 규칙으로 `"<라벨> (<확신도>)"`를 반환하세요.

1. 0 미만이거나 1 초과면 `"invalid"`
2. 라벨: 0.5 이상이면 `positive`, 아니면 `negative`
3. 확신도:
   - 0.9 이상이거나 0.1 이하 → `high`
   - 0.4 초과 0.6 미만 → `low`
   - 그 외 → `medium`

| 입력 | 출력 |
| --- | --- |
| `"0.97"` | `"positive (high)"` |
| `"0.03"` | `"negative (high)"` |
| `"0.5"` | `"positive (low)"` |
| `"0.75"` | `"positive (medium)"` |
| `"0.4"` | `"negative (medium)"` |
| `"1.2"` | `"invalid"` |

## 문제 5 (도전) 학습 계속할까, 멈출까? (Early Stopping)

딥러닝은 매 epoch이 끝날 때 검증 손실(`val_loss`)을 보고 다음 행동을 정합니다.

| 인자 | 의미 |
| --- | --- |
| `epoch`, `max_epochs` | 지금 끝난 epoch 번호, 최대 epoch 수 |
| `val_loss` | 이번 epoch의 검증 손실 (작을수록 좋음) |
| `best_loss` | 지금까지 최저 손실. **첫 epoch에는 기록이 없어서 `None`** |
| `bad_epochs` | 이번 epoch **전까지** 연속으로 개선되지 않은 epoch 수 |
| `patience` | 연속으로 몇 번까지 개선이 없어도 참을지 |

규칙:

1. **개선**: `best_loss`가 `None`이거나 `val_loss < best_loss`이면 개선입니다. (같으면 개선 아님)
2. 개선됐으면 → `"save"`. 단, 마지막 epoch(`epoch >= max_epochs`)이면 `"save, stop"`
3. 개선 안 됐고 마지막 epoch이면 → `"stop"`
4. 개선 안 됐고, 이번까지 합친 연속 미개선 횟수(`bad_epochs + 1`)가 `patience` 이상이면 → `"stop"`
5. 그 외 → `"wait"`

| epoch, max | val_loss | best_loss | bad_epochs | patience | 출력 |
| --- | --- | --- | --- | --- | --- |
| 1, 10 | 0.9 | `None` | 0 | 3 | `"save"` |
| 5, 10 | 0.4 | 0.5 | 2 | 3 | `"save"` |
| 5, 10 | 0.5 | 0.5 | 0 | 3 | `"wait"` |
| 5, 10 | 0.6 | 0.5 | 2 | 3 | `"stop"` |
| 10, 10 | 0.3 | 0.5 | 0 | 3 | `"save, stop"` |
| 3, 10 | 0.1 | **0.0** | 0 | 3 | `"wait"` |

마지막 줄을 꼭 생각해 보세요. 손실이 0.0인 기록이 있다는 건 "기록 없음"과 다릅니다.

---

## 힌트 (막혔을 때만 펼쳐 보세요)

<details>
<summary>문제 1 힌트</summary>

"이상"은 `>=`입니다. `>`를 쓰면 `0.5, 0.5`에서 틀립니다.
</details>

<details>
<summary>문제 2 힌트</summary>

`invalid` 검사를 **가장 먼저** 하세요. 그다음 90 → 80 → 70 → 60 순서로 elif를 쓰면, 각 elif에서 상한을 다시 쓸 필요가 없습니다. `0 <= score <= 100` 같은 연쇄 비교에 `not`을 붙이는 방법도 있습니다.
</details>

<details>
<summary>문제 3 힌트</summary>

"나누어떨어진다" = `year % 4 == 0`. 예외가 있는 규칙은 "가장 특별한 경우부터" if로 검사하면 쉽습니다: 400 → 100 → 4. 익숙해지면 `and`/`or`로 한 줄 `return`도 가능합니다.
</details>

<details>
<summary>문제 4 힌트</summary>

1. `p = float(prob_text)` 먼저.
2. invalid 이면 바로 `return "invalid"` (early return).
3. 라벨과 확신도를 각각 변수에 담은 뒤, 마지막에 f-string으로 합치세요.
4. "0.4 초과 0.6 미만"은 `0.4 < p < 0.6`.
</details>

<details>
<summary>문제 5 힌트 1 — 개선 판단</summary>

`improved = best_loss is None or val_loss < best_loss`. 순서를 바꾸면 `None`일 때 `TypeError`가 납니다(단락 평가). `not best_loss`로 검사하면 `0.0`일 때 틀립니다.
</details>

<details>
<summary>문제 5 힌트 2 — 순서</summary>

`improved`와 `is_last = epoch >= max_epochs`를 변수로 먼저 만들어 두면, 규칙 2~5를 위에서부터 그대로 if/elif로 옮길 수 있습니다. 규칙 2 안에 if가 한 번 더 들어가는 구조입니다.
</details>
