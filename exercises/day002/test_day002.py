"""Day 2 테스트 — 실행: pytest exercises/day002 -v"""
import pytest

from problem_01 import total_score
from problem_02 import format_accuracy
from problem_03 import bmi_report
from problem_04 import is_close
from problem_05 import format_log


# ---------- 문제 1 ----------
@pytest.mark.parametrize(
    "a, b, c, expected",
    [("90", "85", "77", 252), ("0", "0", "0", 0), ("100", "100", "100", 300), ("-5", "10", "3", 8)],
)
def test_total_score(a, b, c, expected):
    result = total_score(a, b, c)
    assert result == expected
    assert isinstance(result, int), "합계는 int 여야 합니다"


# ---------- 문제 2 ----------
@pytest.mark.parametrize(
    "correct, total, expected",
    [
        (875, 1000, "정확도: 87.50%"),
        (1, 3, "정확도: 33.33%"),
        (2, 3, "정확도: 66.67%"),
        (10, 10, "정확도: 100.00%"),
        (0, 7, "정확도: 0.00%"),
    ],
)
def test_format_accuracy(correct, total, expected):
    assert format_accuracy(correct, total) == expected


# ---------- 문제 3 ----------
@pytest.mark.parametrize(
    "w, h, expected",
    [
        ("70", "175", "키 175.0cm, 몸무게 70.0kg → BMI 22.86"),
        ("55.5", "162.3", "키 162.3cm, 몸무게 55.5kg → BMI 21.07"),
        ("90", "180", "키 180.0cm, 몸무게 90.0kg → BMI 27.78"),
        ("48.26", "155", "키 155.0cm, 몸무게 48.3kg → BMI 20.09"),
    ],
)
def test_bmi_report(w, h, expected):
    assert bmi_report(w, h) == expected


# ---------- 문제 4 ----------
@pytest.mark.parametrize(
    "pred, target, tol, expected",
    [
        ("0.30000000000000004", 0.3, 1e-9, True),
        ("0.31", 0.3, 0.001, False),
        ("0.29", 0.3, 0.02, True),
        ("1", 1.0, 0.0, True),
        ("-0.5", 0.5, 0.5, False),
    ],
)
def test_is_close(pred, target, tol, expected):
    result = is_close(pred, target, tol)
    assert result is expected, "True 또는 False (bool) 를 반환해야 합니다"


# ---------- 문제 5 ----------
@pytest.mark.parametrize(
    "args, expected",
    [
        (("3", "10", "0.123456", "0.925"), "Epoch 03/10 | loss 0.1235 | acc 92.5%"),
        (("7", "100", "2.5", "0.1"), "Epoch 007/100 | loss 2.5000 | acc 10.0%"),
        (("1", "5", "1.23456789", "0.33333"), "Epoch 1/5 | loss 1.2346 | acc 33.3%"),
        (("12", "12", "0.00012", "1"), "Epoch 12/12 | loss 0.0001 | acc 100.0%"),
        (("42", "1000", "0.05", "0.8771"), "Epoch 0042/1000 | loss 0.0500 | acc 87.7%"),
    ],
)
def test_format_log(args, expected):
    assert format_log(*args) == expected
