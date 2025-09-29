import builtins
import pytest
from calculator.cli import run_repl


def feed_inputs(*items):
    """Helper to generate a deterministic input() function from a list."""
    data = list(items)

    def _fake_input(prompt: str) -> str:  # noqa: ARG001 - used by interface
        return data.pop(0)

    return _fake_input


def test_cli_happy_path_add(capsys):
    inputs = (
        "add",  # choose operation
        "2",    # a
        "3",    # b
        "quit", # exit
    )

    run_repl(input_fn=feed_inputs(*inputs))
    out = capsys.readouterr().out
    assert "Result: 5.0" in out
    assert "Goodbye!" in out


def test_cli_invalid_operation_then_quit(capsys):
    inputs = (
        "noop",  # invalid
        "quit",
    )
    run_repl(input_fn=feed_inputs(*inputs))
    out = capsys.readouterr().out
    assert "Unknown operation" in out
    assert "Goodbye!" in out


def test_cli_invalid_number_then_recover(capsys):
    inputs = (
        "mul",
        "abc",  # invalid first number
        # after error, REPL loops back to prompt; we try again
        "mul",
        "4",
        "2",
        "quit",
    )
    run_repl(input_fn=feed_inputs(*inputs))
    out = capsys.readouterr().out
    assert "Invalid number" in out
    assert "Result: 8.0" in out


def test_cli_divide_by_zero(capsys):
    inputs = (
        "div",
        "10",
        "0",
        "quit",
    )
    run_repl(input_fn=feed_inputs(*inputs))
    out = capsys.readouterr().out
    assert "Cannot divide by zero." in out
    assert "Goodbye!" in out

def test_cli_unexpected_exception_branch(capsys, monkeypatch):
    # Patch Calculator.add to raise at runtime
    import calculator.cli as cli

    def boom(self, a, b):
        raise RuntimeError("boom")

    monkeypatch.setattr(cli.Calculator, "add", boom)

    inputs = ("add", "1", "2", "quit")
    run_repl(input_fn=feed_inputs(*inputs))
    out = capsys.readouterr().out
    assert "Unexpected error: boom" in out
    assert "Goodbye!" in out

def test_cli_unexpected_exception_branch(capsys, monkeypatch):
    # Patch Calculator.add to raise at runtime
    import calculator.cli as cli

    def boom(self, a, b):
        raise RuntimeError("boom")

    monkeypatch.setattr(cli.Calculator, "add", boom)

    inputs = ("add", "1", "2", "quit")
    run_repl(input_fn=feed_inputs(*inputs))
    out = capsys.readouterr().out
    assert "Unexpected error: boom" in out
    assert "Goodbye!" in out

def test_cli_module_main_guard(monkeypatch, capsys):
    """
    Covers: `if __name__ == "__main__": run_repl()`
    Executes the module as a script and feeds 'quit' so it exits immediately.
    """
    import builtins, runpy

    inputs = iter(["quit"])
    monkeypatch.setattr(builtins, "input", lambda _="": next(inputs))

    # Run the module as if `python -m calculator.cli` was invoked
    runpy.run_module("calculator.cli", run_name="__main__")

    out = capsys.readouterr().out
    assert "Goodbye!" in out
