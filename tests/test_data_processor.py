import unittest
import os
import sys
import random
import pdb
import csv
sys.path.append('../')
import data_processor as proc  # nopep8


class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        self.test_empty_file = 'test_empty.data'
        f = open(self.test_empty_file, 'w')
        f.close()

    def test_get_rand_mat_empty(self):
        self.assertRaises(TypeError, proc.get_random_matrix, None, None)
        self.assertRaises(TypeError, proc.get_random_matrix, 'hi', 'bye')
        self.assertRaises(TypeError, proc.get_random_matrix, 0.2, 0.2)

    def test_get_rand_mat_fill(self):
        random.seed(1)
        randno = random.random()
        random.seed(1)
        r = proc.get_random_matrix(14, 14)
        self.assertEqual(r[0][0], randno)
        self.assertTrue(r[0][0] < 1)

    def test_get_file_dim_known(self):
        r = proc.get_file_dimensions('../iris.data', ',')
        self.assertEqual(r, (150, 5))

    def test_get_file_dim_nofile(self):
        self.assertRaises(FileNotFoundError,
                          proc.get_file_dimensions,
                          'fake.txt',
                          ',')

    def test_get_file_dim_empty(self):
        self.assertRaises(TypeError, proc.get_file_dimensions,
                          self.test_empty_file, ',')

    def test_write_mat(self):
        r = proc.write_matrix_to_file(None, None, None)
        self.assertEqual(r, None)

    def tearDown(self):
        os.remove(self.test_empty_file)


if __name__ == '__main__':
    unittest.main()
