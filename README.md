# Prolog Interpreter (Python)

A minimal Prolog interpreter implemented in Python. Supports basic facts, rules, unification, backtracking, and interactive query evaluation via a REPL.

---

## Installation (with uv)

Clone this repository and create the environment with [uv](https://github.com/astral-sh/uv).

```bash
git clone https://github.com/kubotadaichi/prolog.git & cd prolog
uv sync
source .venv/bin/activate
```

## USAGE
### 1. Write a knowledge base (e.g., `input.pl`)
```prolog
parent(john, mary).
parent(john, anne).
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
```
### 2. Start the REPL
```bash
uv run repl.py input.pl
Welcome to the Prolog REPL! (type 'halt.' to exit)
| ?-
```
### 3. Run queries

