import unittest
import task
from datetime import date


class TestCase(unittest.TestCase):

    def test_calc_area(self):
        area = task.calc_area(2)
        self.assertEqual(12.566370614359172, area)

    def test_first_last(self):
        list = [1, 3, 5, 7]
        listResult = task.first_last(list)
        self.assertEqual([1, 7], listResult)

    def test_calc_days(self):
        first = date(2020, 2, 1)
        last = date(2020, 2, 10)
        days = task.calc_days(first, last)
        self.assertEqual(9, days)


if __name__ == '__main__':
    unittest.main()
