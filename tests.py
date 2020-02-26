import unittest
import task


class TestCase(unittest.TestCase):

    def test_calc_area(self):
        area = task.calc_area(2)
        self.assertEqual(12.566370614359, area)
