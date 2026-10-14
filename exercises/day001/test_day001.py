"""Day 1 테스트 — 실행: pytest exercises/day001 -v"""
import pytest

from problem_01 import celsius_to_fahrenheit
from problem_02 import make_greeting
from problem_03 import seconds_to_hms
from problem_04 import count_batches
from problem_05 import batch_summary


# ---------- 문제 1 ----------
@pytest.mark.parametrize(
    "c, expected",
    [(0, 32.0), (100, 212.0), (-40, -40.0), (36.5, 97.7)],
)
def test_celsius_to_fahrenheit(c, expected):
    assert celsius_to_fahrenheit(c) == pytest.approx(expected)


def test_celsius_returns_float():
    assert isinstance(celsius_to_fahrenheit(10), float)


# ---------- 문제 2 ----------
@pytest.mark.parametrize(
    "name, age, expected",
    [
        ("민수", 25, "안녕하세요, 민수님! 내년에는 26살이 되시네요."),
        ("Alice", 0, "안녕하세요, Alice님! 내년에는 1살이 되시네요."),
        ("지혜", 99, "안녕하세요, 지혜님! 내년에는 100살이 되시네요."),
    ],
)
def test_make_greeting(name, age, expected):
    assert make_greeting(name, age) == expected


# ---------- 문제 3 ----------
@pytest.mark.parametrize(
    "secs, expected",
    [
        (3725, "1시간 2분 5초"),
        (59, "0시간 0분 59초"),
        (60, "0시간 1분 0초"),
        (0, "0시간 0분 0초"),
        (86399, "23시간 59분 59초"),
        (90061, "25시간 1분 1초"),
    ],
)
def test_seconds_to_hms(secs, expected):
    assert seconds_to_hms(secs) == expected


# ---------- 문제 4 ----------
@pytest.mark.parametrize(
    "n, b, expected",
    [(1000, 32, 32), (64, 32, 2), (5, 10, 1), (1, 1, 1), (33, 32, 2), (60000, 128, 469)],
)
def test_count_batches(n, b, expected):
    result = count_batches(n, b)
    assert result == expected
    assert isinstance(result, int), "배치 개수는 int 여야 합니다 (float 아님)"


# ---------- 문제 5 ----------
@pytest.mark.parametrize(
    "n, b, expected",
    [
        (1000, 32, "샘플 1000개 / 배치 크기 32 → 배치 32개, 마지막 배치 8개"),
        (64, 32, "샘플 64개 / 배치 크기 32 → 배치 2개, 마지막 배치 32개"),
        (5, 10, "샘플 5개 / 배치 크기 10 → 배치 1개, 마지막 배치 5개"),
        (60000, 128, "샘플 60000개 / 배치 크기 128 → 배치 469개, 마지막 배치 96개"),
    ],
)
def test_batch_summary(n, b, expected):
    assert batch_summary(n, b) == expected
