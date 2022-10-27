import unittest
import os
import sys
import random
import pdb
sys.path.append("..")
import data_processor as proc #nopep8


class TestDataProcessor(unittest.TestCase):
    def test_get_rand_mat_empty(self):
        self.assertRaises(TypeError, proc.get_random_matrix, None, None)

    def test_get_rand_mat_fill(self):
        random.seed(1)
        randno = random.random()
        random.seed(1)
        r = proc.get_random_matrix(14, 14)
        self.assertEqual(r[0][0], randno)

if __name__ == '__main__':
    unittest.main()

