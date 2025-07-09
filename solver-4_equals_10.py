"""
Solves problems from the '4=10' game. It generates all possible combinations of the given digits and allowed operations,
and prints out all expressions that evaluate to 10. If the input digits contain duplicates, duplicate expressions may occur.

Usage:
    python solver-4_equals_10.py --numbers 1234 --operations "+" --no-brackets
    python solver-4_equals_10.py --numbers 7112 --operations "+-*"
    python solver-4_equals_10.py --numbers 1598

Arguments:
    --numbers, --nums (str, required):
        Exactly four digits to be used in the expressions (e.g. "1234").

    --operations, --ops (str, optional, default: "+-*/"):
        Allowed operations to insert between digits. Must be a subset of '+-*/'.

    --no-brackets (flag, optional):
        Disables the use of brackets in expressions. By default, brackets are allowed.

Output:
    Prints all expressions that evaluate to 10 to the standard output.
"""

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--numbers", "--nums", type=str, required=True,
                    help="Exactly 4 digits to use in the expressions (e.g. '1234')")
parser.add_argument("--operations", "--ops", type=str, default="+-*/",
                    help="Allowed operations to use between digits (subset of '+-*/')")
parser.add_argument("--no-brackets", action="store_false", dest="brackets",
                    help="Disable brackets in expressions")


args = parser.parse_args()

if len(args.numbers) != 4 or not args.numbers.isdigit():
    raise Exception("Argument --numbers must contain exactly 4 digits")

if 1 > len(args.operations) > 4 or any(o not in "+-*/" for o in args.operations) or len(set(args.operations)) < len(args.operations):
    raise Exception("Argument --operations must be a subset of '+-*/' and cannot have duplicates")


def remove_digit(numbers: str, number: str) -> str:
    i = numbers.index(number)
    return numbers[:i] + numbers[i+1:]


def check_10(exp: str):
    try:
        r = eval(exp)
        if r == 10:
            print(exp)
    except ZeroDivisionError:
        pass


def try_brackets(exp: str):
    if not args.brackets:
        check_10(exp)
        return

    for i in range(0, len(exp), 2):
        s = exp[:i] + "(" + exp[i:]
        for j in range(i + 4, len(exp) + 2, 2):
            res = s[:j] + ")" + s[j:]

            check_10(res)


def append_number(exp: str, possible_numbers: str):
    if not possible_numbers:
        try_brackets(exp)
        return

    for i in possible_numbers:
        if len(possible_numbers) == 1:
            append_number(exp + i, "")
        else:
            for o in args.operations:
                append_number(exp + i + o, remove_digit(possible_numbers, i))


append_number("", args.numbers)
