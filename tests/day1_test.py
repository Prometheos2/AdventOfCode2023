from src import day1A
from src import day1B


class TestDay1A:
    verification = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".splitlines()

    expected = 142

    def test_proposal_no1(self):
        assert day1A.proposal_no1(self.verification) == self.expected

    def test_proposal_no2(self):
        assert day1A.proposal_no2(self.verification) == self.expected


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
