"""Spreadsheet Column Printer

This script allows the user to print to the console all columns in the
spreadsheet. It is assumed that the first row of the spreadsheet is the
location of the columns.

This tool accepts comma separated value files (.csv) as well as excel
(.xls, .xlsx) files.

This script requires that `pandas` be installed within the Python
environment you are running this script in.

This file can also be imported as a module and contains the following
functions:

    * get_spreadsheet_cols - returns the column headers of the file
    * main - the main function of the script
"""

import sys
import time
import subprocess
from contextlib import redirect_stdout

def eval_function():
    """
    Function get list of source code files and execute it using subprocess library
    :param argv: arguments from sys lib
    :return: None
    """
    if len(sys.argv) <= 1:
        # print(sys.argv[0])
        help(sys.argv[0].replace('.py', ''))
        return

    args = sys.argv[1:]
    func2time = {}
    with open('stdout.txt', 'a') as f:
        with redirect_stdout(f):
            for scr in args:
                start_time = time.time()
                subprocess.run(['python3', scr])
                executed_time = time.time() - start_time
                func2time.update({scr : executed_time})
    
    sorted_exec = sorted(func2time.items(), key = lambda func_time: func_time[1])
    print("{0:15} {1:} {2:15}".format("Script", "|RANK", "|TIME ELAPSED"))
    rank_order = 0
    for func, func_time in (sorted_exec):
        rank_order += 1
        print('{0:15} {1:} {2:15}s'.format(func, rank_order, round(func_time,8)))

if __name__ == "__main__":
    eval_function()