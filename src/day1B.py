from pathlib import Path

# Ordered so any "eightwo" is properly converted to "8wo"
REPLACEMENT_TABLE: dict = {
    "threeight": "3",  # edge case
    "eightwo": "8",  # edge case
    "two": "2",
    "one": "1",
    "five": "5",
    "seven": "7",
    "nine": "9",
    "eight": "8",
    "three": "3",
    "four": "4",
    "six": "6",
}


# Non functional; "too small"
def proposal_no1(input_file: str) -> int:
    for criteria in REPLACEMENT_TABLE:

        input_file = input_file.replace(criteria, REPLACEMENT_TABLE[criteria])

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
