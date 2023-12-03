import re
from collections.abc import Sequence
from pathlib import Path


def proposal_no1(input_lines: Sequence[str]) -> int:
    res = 0
    regex: re.Pattern[str] = re.compile(r"\d")
    for line in input_lines:
        matches: list[str] = regex.findall(line)
        number: str = matches[0] + matches[-1]
        res += int(number)

    return res


def proposal_no2(input_lines: Sequence[str]) -> int:
    res = 0
    for line in input_lines:
        digits = list(filter(str.isnumeric, line))
        number: str = digits[0] + digits[-1]
        res += int(number)

    return res


if __name__ == "__main__":
    with Path.open("inputs/day1.txt") as file:
        input_lines: list[str] = file.readlines()

    print(proposal_no2(input_lines))
