import unittest
from txt2csv.txt2output import *
import numpy

class TestTxt2csv(unittest.TestCase):
    def test_columns(self):
        txt = Txt2csv('data/input.txt', 'data/specifications.txt')
        addcols_dict = {'Total_Transaction_Amount':['Quantity_Long', '-', 'Quantity_Short']}
        txt.addCols(addcols_dict)
        self.assertIn('Total_Transaction_Amount',txt.df.columns)

    def test_csvheaders1(self):
        txt = Txt2csv('data/input.txt', 'data/specifications.txt')
        addcols_dict = {'Total_Transaction_Amount':['Quantity_Long', '-', 'Quantity_Short']}
        outputcols_dict = {'Client_Information':['Client_Type', 'Client_Number', 'Account_Number', 'Subaccount_Number'],
                        'Product_Information':['Exchange_Code', 'Product_Group_Code', 'Symbol', 'Expiration_Date']
                        }
        output_csv_headers = ['Client_Information', 'Product_Information', 'Total_Transaction_Amount']
        txt.addCols(addcols_dict)
        txt.createOutputFile(outputcols_dict, groupby_col='Total_Transaction_Amount', csv_headers = output_csv_headers)
        df = pd.read_csv('Output.csv')
        numpy.testing.assert_array_equal(output_csv_headers, df.columns)
        
if __name__== "__main__":
    unittest.main()

    