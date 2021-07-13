import unittest
from txt2csv import *


class TestTxt2csv(unittest.TestCase):

    def test_columns(self):

        t = Txt2csv('data/input.txt', 'data/specifications.txt')
        addcols_dict = {'Total':['Quantity_long', '-', 'Quantity_Short']}
        t.addCols(addcols_dict)
        assert 'Total' in t.df.columns
    