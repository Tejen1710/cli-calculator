"""Command-line REPL for the calculator with input validation & errors."""

from __future__ import annotations
from typing import Callable, Dict
from .calculator import Calculator

PROMPT = (
    "\nCalculator REPL\n"
    "Choose an operation: add, sub, mul, div\n"
    "Or type 'quit' to exit.\n> "
)


def _parse_number(text: str) -> float:
    try:
        return float(text)
    except ValueError as exc:
        raise ValueError(f"Invalid number: '{text}'.") from exc


def _get_numbers(input_fn: Callable[[str], str]) -> tuple[float, float]:
    a = _parse_number(input_fn("Enter first number: "))
    b = _parse_number(input_fn("Enter second number: "))
    return a, b


def run_repl(input_fn=input, output_fn=print) -> None:
    calc = Calculator()
    ops: Dict[str, Callable[[float, float], float]] = {
        "add": calc.add,
        "sub": calc.sub,
        "mul": calc.mul,
        "div": calc.div,
    }

    while True:
        cmd = input_fn(PROMPT).strip().lower()
        if cmd in {"quit", "exit", "q"}:
            output_fn("Goodbye!")
            break

        if cmd not in ops:
            output_fn("Unknown operation. Please choose: add, sub, mul, div, or 'quit'.")
            continue

        try:
            a, b = _get_numbers(input_fn)
            result = ops[cmd](a, b)
            output_fn(f"Result: {result}")
        except ValueError as ve:
            output_fn(str(ve))
        except ZeroDivisionError as zde:
            output_fn(str(zde))
        except Exception as e:  # defensive programming; keeps REPL alive
            output_fn(f"Unexpected error: {e}")


if __name__ == "__main__":
    run_repl()