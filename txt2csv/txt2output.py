"""
Python code to convert the input.txt file to output.csv file

pip3 install -e .
python txt2output.py
python test_columns.py

"""
import pandas as pd
import operator
import logging

#class to perform the necessary transformations and then store the data in output csv using its reusable methods
class Txt2csv:
    def __init__(self, input_file_name, specs_file_name):
        self.df = pd.read_csv(input_file_name, names=['Input']) #read the input.txt file as a pandas dataframe
        self.specs_file_name = specs_file_name #input the specifications.txt file name
        self.start_idx = None #slicing index start value
        self.last_idx = None #slicing index last value
        self.txt2df()

    #create new columns in the dataframe based on the column name and length specified in the specifications.txt file
    def txt2df(self): 
        try:
            with open(self.specs_file_name, "r") as specs:
                for line in specs:
                    stripped_line = line.strip()
                    split_line = stripped_line.split(',')
                    if self.start_idx == None:
                        self.last_idx = 0 + int(split_line[1])
                    else:
                        self.last_idx = self.start_idx + int(split_line[1])
                    self.df[split_line[0]] = self.df.apply(lambda x: x['Input'][self.start_idx:self.last_idx], axis=1)
                    self.start_idx = self.last_idx
            if self.last_idx == 176:
                logging.debug(f'All columns created from {self.specs_file_name}!')
            else:
                logging.info(f'Some columns are missing from {self.specs_file_name}')
        except:
            logging.error(f"Failed to create columns from {self.specs_file_name}!")

    #add new column according to the input arithmatic operator 
    def addCols(self, addcols_dict):
        ops = {'+': operator.add, '-': operator.sub, 'x': operator.mul}
        for key,value in addcols_dict.items():
            try:
                self.df[key] = ops[value[1]](self.df[value[0]].astype('float'), self.df[value[2]].astype('float'))
                logging.debug(f'{key} column successfully added!')
            except:
                logging.error(f'Failed to create {key} column!')

    #create output csv file based on the input parameters
    def createOutputFile(self, outputcols_dict, groupby_col, csv_headers):
            df_output_cols = []
            try:
                for key, value in outputcols_dict.items():
                    df_output_cols += value
                df_output = self.df.groupby(df_output_cols, as_index=False)[groupby_col].sum()
                for key, value in outputcols_dict.items():
                    df_output[key] = df_output[value].apply(lambda row: '_'.join(row.values.astype(str)), axis=1)
                df_final_output = df_output[csv_headers]
                df_final_output.to_csv('Output.csv', index=False)
                logging.debug('Successfuly created output.csv!')
            except:
                logging.error('Failed to create output.csv!')

if __name__ == '__main__':

    addcols_dict = {'Total_Transaction_Amount':['Quantity_Long', '-', 'Quantity_Short']} #dictionary to add the column in the dataframe based on some operation
    outputcols_dict = {'Client_Information':['Client_Type', 'Client_Number', 'Account_Number', 'Subaccount_Number'],
                        'Product_Information':['Exchange_Code', 'Product_Group_Code', 'Symbol', 'Expiration_Date']
                        } #dictionary to add header names to the output csv
    output_csv_headers = ['Client_Information', 'Product_Information', 'Total_Transaction_Amount'] #final output csv headers in order
    logging.basicConfig(level=logging.DEBUG, filename='log', format='%(asctime)s %(levelname)s:%(message)s') #initialise log file and set its logging level
    t = Txt2csv('data/input.txt', 'data/specifications.txt') #initialise the class
    t.addCols(addcols_dict) #add the new column by calling the method from the class object
    t.createOutputFile(outputcols_dict, groupby_col='Total_Transaction_Amount', csv_headers = output_csv_headers) #create the output csv file by calling the method from the class object
