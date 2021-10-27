"""TODO: add brackets in equation, optimise performance"""

import itertools
from timeout import timeout, TimeoutError

TARGET = 404
CARRIAGE_DIGITS = 4
OPERATIONS = ["+", "-", "*", "/", "**", "%"]
OPERATIONS_PERM = tuple(itertools.product(OPERATIONS, repeat=CARRIAGE_DIGITS - 1))


def generate_equation(digits: list[str], operations: tuple[str, ...]) -> list[str]:
    # equation = []
    # for i in range(CARRIAGE_DIGITS - 1):
    #     equation.append(digits[i])
    #     equation.append(operations[i])
    # equation.append(digits[-1])
    # return equation
    equation = []
    for tup in zip(digits, operations):
        equation.extend(tup)
    equation.append(digits[-1])
    return equation


@timeout(1)
def calculate_equation(equation: str) -> int:
    return eval(equation)


def train(carriage: int) -> list[str]:
    # print(carriage)
    solutions = []
    digits = list(str(carriage))
    # try all operations
    for operations in OPERATIONS_PERM:
        equation = " ".join(generate_equation(digits, operations))
        try:
            if calculate_equation(equation) == TARGET:
                equation = equation.replace("**", "^")
                solutions.append(equation)
        except Exception:
            # except (ZeroDivisionError, SyntaxError, TypeError, TimeoutError):
            # print(equation)
            pass
    return solutions


if __name__ == "__main__":
    # generate carriage numbers
    LOWEST_CARRIAGE = 10 ** (CARRIAGE_DIGITS - 1)
    HIGHEST_CARRIAGE = 10 ** CARRIAGE_DIGITS
    for carriage in range(LOWEST_CARRIAGE, HIGHEST_CARRIAGE):
        if carriage % 500 == 0:
            print(carriage)
        if solutions := train(carriage):
            print(f"{carriage=}")
            print(*solutions, sep="\n")
