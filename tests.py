import unittest
import task


class TestCase(unittest.TestCase):
    def test_areaFromRadius(self):
        self.assertEqual(78.5, task.areaFromRadius(5))


if __name__ == '__main__':
    unittest.main()
