import unittest
from txt2csv import *


class TestTxt2csv(unittest.TestCase):
    def setUp(self):
        self.txt = Txt2csv('data/input.txt', 'data/specifications.txt')

    def tearDown(self):
        addcols_dict = {'Total_Transaction_Amount':['Quantity_Long', '-', 'Quantity_Short']}
        self.txt.addCols(addcols_dict)

    def test_columns(self):
        # print(self.txt.df.info())
        self.assertIn('Total_Transaction_Amount',self.txt.df.columns)

if __name__== "__main__":
    unittest.main()
    # test = TestTxt2csv()
    # test.test_columns()
    # print("All tests passed!")
    