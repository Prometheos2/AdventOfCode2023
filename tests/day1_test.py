from src import day1A


def test_day1A():
    verification = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".split("\n")

    expected = 142

    assert day1A.main(verification) == expected
