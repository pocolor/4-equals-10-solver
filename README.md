# 4=10 Solver

Solves problems from the **"4=10"** game. It generates all possible expressions using the given four digits and allowed operations, and prints those that evaluate to **10**. If the input digits contain duplicates, duplicate expressions may occur in the output.

---

### Usage

```bash
python solver-4_equals_10.py --numbers 1234 --operations "+" --no-brackets
python solver-4_equals_10.py --numbers 7112 --operations "+-*"
python solver-4_equals_10.py --numbers 1598
```

### Arguments
* `--numbers`, `--nums` (str, required):  
Exactly four digits to be used in the expressions (e.g. `"1234"`).

* `--operations`, `--ops` (str, optional, default: `"+-*/"`):  
Allowed operations to insert between digits. Must be a subset of `+-*/`.

* `--no-brackets` (flag, optional):  
Disables the use of brackets in expressions. By default, brackets are allowed.

### Output
Prints all expressions that evaluate to 10 to the standard output.
