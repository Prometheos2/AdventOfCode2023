from pathlib import Path

REPLACEMENT_TABLE: dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


# Non functional; "too small"
def proposal_no1(input_file: str) -> int:
    for criteria in REPLACEMENT_TABLE:
        # eightwo => 8eight2two, to avoid eightwo => eigh2 (which is incorrect)
        input_file = input_file.replace(
            criteria, criteria + REPLACEMENT_TABLE[criteria]
        )

    res = 0
    lines: list[str] = input_file.splitlines()
    for line in lines:
        digits = list(filter(str.isnumeric, line))
        number: str = digits[0] + digits[-1]
        print(number)
        res += int(number)

    return res


if __name__ == "__main__":
    with Path.open("inputs/day1.txt") as file:
        input_file: list[str] = file.read()

    print(proposal_no1(input_file))
