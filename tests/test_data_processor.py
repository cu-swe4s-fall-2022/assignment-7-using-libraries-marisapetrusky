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
        self.test_write_file = 'test_write.csv'

    def test_get_rand_mat_empty(self):
        self.assertRaises(TypeError, proc.get_random_matrix, None, None)
        self.assertRaises(TypeError, proc.get_random_matrix, 'hi', 'bye')
        self.assertRaises(TypeError, proc.get_random_matrix, 0.2, 0.2)

    def test_get_rand_mat_fill(self):
        random.seed(1)
        randno = random.random()
        random.seed(1)
        r = proc.get_random_matrix(1, 1)
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
        self.assertRaises(TypeError,
                          proc.get_file_dimensions,
                          self.test_empty_file,
                          ',')

    def test_write_mat(self):
        num_rows = random.randint(1, 15)
        num_columns = random.randint(1, 15)
        r = proc.write_matrix_to_file(num_rows,
                                      num_columns,
                                      self.test_write_file)
        try:
            r = proc.get_file_dimensions(self.test_write_file, ',')
            self.assertEqual(r[0], num_rows)
            self.assertEqual(r[1], num_columns)
        except:
            self.fail('write_matrix_to_file did not create file')

    def test_write_mat_no_fname(self):
        self.assertRaises(TypeError,
                          proc.write_matrix_to_file,
                          1,
                          1,
                          22)

    def test_write_mat_not_csv(self):
        self.assertRaises(TypeError,
                          proc.write_matrix_to_file,
                          1,
                          1,
                          'test.txt')

    def tearDown(self):
        os.remove(self.test_empty_file)


if __name__ == '__main__':
    unittest.main()
