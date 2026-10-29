"""Day 4 테스트 — 실행: pytest exercises/day004 -v"""
import pytest

from problem_01 import sum_to_n
from problem_02 import count_char
from problem_03 import is_prime
from problem_04 import sum_log_digits
from problem_05 import steps_to_converge


# ---------- 문제 1 ----------
@pytest.mark.parametrize(
    "n, expected",
    [(5, 15), (1, 1), (2, 3), (10, 55), (100, 5050), (0, 0), (-3, 0)],
)
def test_sum_to_n(n, expected):
    assert sum_to_n(n) == expected


# ---------- 문제 2 ----------
@pytest.mark.parametrize(
    "text, target, expected",
    [
        ("banana", "a", 3),
        ("banana", "b", 1),
        ("banana", "z", 0),
        ("Deep Learning", "e", 3),
        ("Deep Learning", "D", 1),
        ("Deep Learning", "d", 0),
        ("hello world", " ", 1),
        ("", "a", 0),
        ("aaaa", "a", 4),
    ],
)
def test_count_char(text, target, expected):
    assert count_char(text, target) == expected


# ---------- 문제 3 ----------
@pytest.mark.parametrize(
    "n, expected",
    [
        (2, True), (3, True), (5, True), (29, True), (97, True), (7919, True),
        (1, False), (0, False), (-7, False),
        (4, False), (9, False), (25, False), (49, False), (121, False), (7917, False),
    ],
)
def test_is_prime(n, expected):
    assert is_prime(n) is expected


def test_is_prime_large():
    assert is_prime(1000003) is True
    assert is_prime(999983) is True
    assert is_prime(1000001) is False


# ---------- 문제 4 ----------
@pytest.mark.parametrize(
    "line, expected",
    [
        ("a1b2c3", 6),
        ("loss=0.25#epoch9", 7),
        ("epoch 10", 1),
        ("#123", 0),
        ("no digits", 0),
        ("", 0),
        ("999", 27),
        ("acc 0.98 # best 1.00", 17),
        ("7#", 7),
    ],
)
def test_sum_log_digits(line, expected):
    assert sum_log_digits(line) == expected


# ---------- 문제 5 ----------
@pytest.mark.parametrize(
    "w, lr, expected",
    [
        (0, 0.1, 16),
        (0, 0.4, 3),
        (0, 0.5, 1),
        (3, 0.1, 0),
        (2.95, 0.1, 0),
        (10, 0.05, 41),
        (6, 0.3, 4),
        (0, 0.01, 169),
        (0, 1.0, -1),
        (0, 1.1, -1),
        (0, 0.001, -1),
    ],
)
def test_steps_to_converge(w, lr, expected):
    assert steps_to_converge(w, lr) == expected


def test_steps_to_converge_max_steps_boundary():
    assert steps_to_converge(0, 0.1, max_steps=16) == 16
    assert steps_to_converge(0, 0.1, max_steps=15) == -1
    assert steps_to_converge(3, 0.1, max_steps=0) == 0
    assert steps_to_converge(0, 0.1, max_steps=0) == -1


def test_steps_to_converge_custom_tol():
    assert steps_to_converge(0, 0.1, tol=1.0) == 5
    assert steps_to_converge(0, 0.5, tol=0.0) == -1
