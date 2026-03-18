import sys
from pathlib import Path
import unittest

# 讓 tests 可以匯入同層目錄下的解答程式
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import question_948
import question_948_easy
import question_10008
import question_10008_easy
import question_10019
import question_10019_easy
import question_10035
import question_10035_easy
import question_10038
import question_10038_easy


class TestQuestion948(unittest.TestCase):
    def test_unique_fake_coin(self):
        data = """1

3 2
1 1 2
<
1 1 3
=
"""
        self.assertEqual(question_948.solve(data), "2")

    def test_ambiguous_coin_returns_zero(self):
        data = """1

2 1
1 1 2
<
"""
        self.assertEqual(question_948.solve(data), "0")

    def test_easy_same_as_main(self):
        data = """2

3 2
1 1 2
<
1 1 3
=

2 1
1 1 2
<
"""
        self.assertEqual(question_948.solve(data), question_948_easy.solve(data))


class TestQuestion10008(unittest.TestCase):
    def test_count_and_sort(self):
        data = """3
ab
BA
z
"""
        expected = "A 2\nB 2\nZ 1"
        self.assertEqual(question_10008.solve(data), expected)

    def test_easy_same_as_main(self):
        data = """2
This is a test.
Count me!
"""
        self.assertEqual(question_10008.solve(data), question_10008_easy.solve(data))


class TestQuestion10019(unittest.TestCase):
    def test_sample_style(self):
        data = """3
265
111
1234
"""
        expected = "3 5\n6 3\n5 5"
        self.assertEqual(question_10019.solve(data), expected)

    def test_easy_same_as_main(self):
        data = """4
1
10
15
100
"""
        self.assertEqual(question_10019.solve(data), question_10019_easy.solve(data))


class TestQuestion10035(unittest.TestCase):
    def test_sample(self):
        data = """123 456
555 555
123 594
0 0
"""
        expected = "No carry operation.\n3 carry operations.\n1 carry operation."
        self.assertEqual(question_10035.solve(data), expected)

    def test_easy_same_as_main(self):
        data = """1 9999
9999 1
0 0
"""
        self.assertEqual(question_10035.solve(data), question_10035_easy.solve(data))


class TestQuestion10038(unittest.TestCase):
    def test_sample(self):
        data = """4 1 4 2 3
5 1 4 2 -1 6
"""
        expected = "Jolly\nNot jolly"
        self.assertEqual(question_10038.solve(data), expected)

    def test_easy_same_as_main(self):
        data = """1 10
4 1 4 2 3
"""
        self.assertEqual(question_10038.solve(data), question_10038_easy.solve(data))


if __name__ == "__main__":
    unittest.main()
