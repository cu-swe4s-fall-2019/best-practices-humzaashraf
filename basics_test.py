import unittest
import get_column_stats

class TestCalc(unittest.TestCase):
	def test_mean(self):
		self.Is(calc.mean_calc())