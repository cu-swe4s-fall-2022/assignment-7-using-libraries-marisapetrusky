import unittest
import os
import sys
sys.path.append('../')
import plotter as plot  # nopep8


class TestPlotter(unittest.TestCase):
    def test_bad_file(self):
        self.assertRaises(FileNotFoundError, plot.plot_iris, 'badfile')
