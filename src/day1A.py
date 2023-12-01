import re
from collections.abc import Sequence
from pathlib import Path


def main(input_lines: Sequence[str]) -> int:
    res = 0
    regex: re.Pattern[str] = re.compile(r"\d")
    for line in input_lines:
        matches: list[str] = regex.findall(line)
        number: str = matches[0] + matches[-1]
        res += int(number)

    return res


if __name__ == "__main__":
    with Path.open("inputs/day1.txt") as file:
        input_lines: list[str] = file.readlines()

    print(main(input_lines))
