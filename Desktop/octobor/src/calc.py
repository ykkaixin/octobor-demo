"""Simple calculator module for demonstration purposes."""

from __future__ import annotations


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def running_total(values: list[float]) -> float:
    """Return the cumulative total of all values."""
    total = 0.0
    for value in values:
        total += value
    return total
