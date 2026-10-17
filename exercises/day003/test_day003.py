"""Day 3 테스트 — 실행: pytest exercises/day003 -v"""
import pytest

from problem_01 import label_prediction
from problem_02 import score_to_grade
from problem_03 import is_leap_year
from problem_04 import confidence_label
from problem_05 import training_decision


# ---------- 문제 1 ----------
@pytest.mark.parametrize(
    "prob, threshold, expected",
    [
        (0.7, 0.5, "positive"),
        (0.5, 0.5, "positive"),
        (0.49, 0.5, "negative"),
        (0.3, 0.2, "positive"),
        (0.85, 0.9, "negative"),
        (0.0, 0.5, "negative"),
    ],
)
def test_label_prediction(prob, threshold, expected):
    assert label_prediction(prob, threshold) == expected


# ---------- 문제 2 ----------
@pytest.mark.parametrize(
    "score, expected",
    [
        (95, "A"), (100, "A"), (90, "A"),
        (89.9, "B"), (80, "B"),
        (75, "C"), (70, "C"),
        (60, "D"), (69.5, "D"),
        (59.9, "F"), (0, "F"),
        (-1, "invalid"), (101, "invalid"), (100.1, "invalid"),
    ],
)
def test_score_to_grade(score, expected):
    assert score_to_grade(score) == expected


# ---------- 문제 3 ----------
@pytest.mark.parametrize(
    "year, expected",
    [(2024, True), (2023, False), (1900, False), (2000, True), (2100, False), (2400, True), (1996, True), (2019, False)],
)
def test_is_leap_year(year, expected):
    result = is_leap_year(year)
    assert result is expected, "True 또는 False(bool)를 반환해야 합니다"


# ---------- 문제 4 ----------
@pytest.mark.parametrize(
    "prob_text, expected",
    [
        ("0.97", "positive (high)"),
        ("0.03", "negative (high)"),
        ("0.9", "positive (high)"),
        ("0.1", "negative (high)"),
        ("1", "positive (high)"),
        ("0", "negative (high)"),
        ("0.5", "positive (low)"),
        ("0.45", "negative (low)"),
        ("0.75", "positive (medium)"),
        ("0.6", "positive (medium)"),
        ("0.4", "negative (medium)"),
        ("0.2", "negative (medium)"),
        ("1.2", "invalid"),
        ("-0.1", "invalid"),
    ],
)
def test_confidence_label(prob_text, expected):
    assert confidence_label(prob_text) == expected


# ---------- 문제 5 ----------
@pytest.mark.parametrize(
    "args, expected",
    [
        ((1, 10, 0.9, None, 0, 3), "save"),          # 첫 epoch: 기록 없음
        ((5, 10, 0.4, 0.5, 2, 3), "save"),           # 개선
        ((5, 10, 0.5, 0.5, 0, 3), "wait"),           # 같으면 개선 아님
        ((5, 10, 0.6, 0.5, 1, 3), "wait"),
        ((5, 10, 0.6, 0.5, 2, 3), "stop"),           # patience 소진
        ((4, 10, 0.7, 0.5, 0, 1), "stop"),           # patience 1
        ((10, 10, 0.3, 0.5, 0, 3), "save, stop"),    # 마지막 epoch 에 개선
        ((10, 10, 0.6, 0.5, 0, 3), "stop"),          # 마지막 epoch
        ((1, 1, 0.9, None, 0, 3), "save, stop"),     # epoch 1개짜리 학습
        ((3, 10, 0.1, 0.0, 0, 3), "wait"),           # 0.0 은 '기록 없음'이 아니다
    ],
)
def test_training_decision(args, expected):
    assert training_decision(*args) == expected
