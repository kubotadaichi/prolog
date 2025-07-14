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
parent(mary, alice).
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

```bash
| ?- parent(john, X).
X = mary ;
X = anne ;
no
| ?- ancestor(john, Y).
Y = mary ;
Y = anne ;
Y = alice ;
no
| ?- halt.
Exiting REPL.
```

## 🧠 Features
* ✅ Facts and rules

* ✅ Variable unification

* ✅ Recursive backtracking

* ✅ Interactive REPL with support for ; to get multiple answers

* ✅ cut operator (!)

## 🚧 Limitations
* ❌ No support for is/2, arithmetic, or built-in predicates

* ❌ No list matching ([H|T])

* ❌ No module system

## License

This project is licensed under the MIT License.  
See the [LICENSE](./LICENSE) file for details.
