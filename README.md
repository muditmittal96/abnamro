Package components:

abnamro (parent directory)
    -- coding_challenge -> contains all the instruction files provided initially
    -- data
        -- input.txt -> contains the initial raw data provided
        -- specifications.txt -> in order to make the code more reusable, "specifications.txt" file has been created from the "System A File Specification.pdf"
    -- examples
        -- scratchpad1 -> playground to test out various logics
        -- scratchpad2 -> playground to test out various logics
    -- tests
        -- test_columns.py -> contains 2 tests to validate the code
    -- txt2csv
        -- __init__.py -> empty package file
        -- txt2output.py -> main code file containing the class
    -- LICENSE -> license file
    -- log -> log file generated from txt2output.py
    -- Output.csv -> output file generated from txt2output.py
    -- README.md -> contains details about the code package
    -- setup.py -> contains the setup tool configurations

Steps to install and run the package:

1) Inside the package directory run the following command to install the setup file.
    pip3 install -e .

2) Run txt2output.py to generate the output.csv and log files.

3) Run the unittest inside the tests folder to futher validate the code.