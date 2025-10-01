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


def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers."""
    return a - b


def divide(a: float, b: float) -> float:
    """Return the quotient of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a: float, b: float) -> float:
    """Return a raised to the power of b."""
    return a ** b


def modulo(a: float, b: float) -> float:
    """Return the remainder of a divided by b."""
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b
