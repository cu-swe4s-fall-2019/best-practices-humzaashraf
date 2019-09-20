import sys
import os
import random
import unittest
import get_column_stats

class TestCalc(unittest.TestCase):

    def setUp(self):

        self.direct_sum = 0
        self.vector = []

        for i in range(100):
            rand_int = random.randint(1,100)
            self.direct_sum += rand_int
            self.vector.append(rand_int)  

        #rand_int_numpy = np.random.randint(100)
        #a = np.random.choice([1, 0], a.shape, p=[.1, .9]).astype(bool)
        #a[mask] = np.nan

        #for i in range(100):
        #rand_int_nan = random

        self.mean = self.direct_sum/100


    def test_mean(self):
        print(self.direct_sum)
        print(self.mean)
        var = get_column_stats.mean_calc(self.vector)
        self.assertEqual(var,self.mean)


if __name__ == '__main__':
    unittest.main()