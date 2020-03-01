import unittest
import task
import datetime


class TestCase(unittest.TestCase):
    def test_areaFromRadius(self):
        self.assertEqual(78.5, task.areaFromRadius(5))

    def test_getListEnds(self):
        self.assertEqual(["first", "last"], task.getListEnds(["first", "second", "middle", "third", "last"]))

    def test_dateDiff(self):
        self.assertEqual(30, task.dateDiff(datetime.datetime(2020, 2, 29), datetime.datetime(2020, 1, 30)))


if __name__ == '__main__':
    unittest.main()
