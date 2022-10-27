import unittest
import os
import sys
sys.path.append("..")
import data_processor as proc #nopep8


class TestDataProcessor(unittest.TestCase):
    def test_get_rand_mat_empty(self):
        r = proc.get_random_matrix(None, None)
        self.assertEqual(r, None)

if __name__ == '__main__':
    unittest.main()

