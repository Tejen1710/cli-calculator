"""Object-Oriented façade around operations, satisfying CLO6."""

from __future__ import annotations
from dataclasses import dataclass
from . import operations


@dataclass
class Calculator:
    """A simple OOP wrapper; state-free but extensible.

    Using a dataclass for future extensibility (e.g., mode, precision),
    while keeping current implementation simple and fully testable.
    """

    def add(self, a: float, b: float) -> float:
        return operations.add(a, b)

    def sub(self, a: float, b: float) -> float:
        return operations.sub(a, b)

    def mul(self, a: float, b: float) -> float:
        return operations.mul(a, b)

    def div(self, a: float, b: float) -> float:
        return operations.div(a, b)