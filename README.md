# CLI Calculator (Python)
![CI](https://github.com/Tejen1710/cli-calculator/actions/workflows/ci.yml/badge.svg)

A robust, fully-tested command-line calculator with an interactive REPL, built using best practices. Includes GitHub Actions CI with 100% coverage enforcement.


## Features
- REPL interface with clear prompts
- Add, subtract, multiply, divide
- Graceful input validation & error messages
- OOP `Calculator` class (CLO6)
- Pytest unit tests (parameterized) with 100% coverage
- CI via GitHub Actions


## Setup


```bash
# 1) Clone or create your repo, then inside project root:
python -m venv .venv


# Windows PowerShell
. .venv/Scripts/Activate.ps1


# macOS/Linux
# source .venv/bin/activate


pip install -r requirements.txt