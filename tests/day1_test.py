from src import day1A
from src import day1B


def test_day1A():
    verification = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".splitlines()

    expected = 142

    assert day1A.main(verification) == expected


class TestDay1B:
    verification = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

    expected = 281

    def test_proposal_no1(self):
        assert day1B.proposal_no1(self.verification) == self.expected
