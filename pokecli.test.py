import unittest
import os
import pokecli

class TestcalculateAvgPoke(unittest.TestCase):
    def test_calculate_avg_pokes(self):
        actual = pokecli.calculateAvg(10, 1, False)
        expected = 'Average Height: 10.0'
        self.assertIn(expected, actual)

if __name__ == '__main__':
    unittest.main()