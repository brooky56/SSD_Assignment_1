"""Execution time compare

Takes N arbitrary .py files and creates a neat table out of their execution time 
starting with the fastest.

This file can also be imported as a module and contains the following
functions:

    * eval_function - provide main logic for comparing execution time
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
        # If no args return help & annotations of the script
        help(sys.argv[0].replace('.py', ''))
        return

    args = sys.argv[1:]
    func2time = {}
    with open('stdout.txt', 'a') as f:
        with redirect_stdout(f):
            for scr in args:
                start_time = time.time()
                # run scripts from arguments list 
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
    # run evaluation
    eval_function()