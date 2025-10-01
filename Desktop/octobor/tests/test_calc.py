"""Tests for calc module."""

from src.calc import add, multiply, running_total


def test_add():
    assert add(2, 3) == 5


def test_multiply():
    assert multiply(4, 5) == 20


def test_running_total():
    assert running_total([1, 2, 3, 4]) == 10
    assert running_total([]) == 0
