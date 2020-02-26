import unittest
import task


class TestCase(unittest.TestCase):

    def test_calc_area(self):
        area = task.calc_area(2)
        self.assertEqual(12.566370614359, area)

    def test_first_last(self):
        list = [1, 3, 5, 7]
        listResult = task.first_last(list)
        self.assertEqual([1, 7], listResult)


if __name__ == '__main__':
    unittest.main()
