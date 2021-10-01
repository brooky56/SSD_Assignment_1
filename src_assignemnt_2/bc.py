"""Opcodes printing and analyze

Namely, look at the bytecode. So our task is to reveal what the beast the bytecode is. To start something from, write a program 
that yield opcodes (and their arguments) for ordinary python programs. 

This file can also be imported as a module and contains the following
functions:

    * expand_bytecode - function find and extends bytecode result
    * compile - function produce (compile) .py files or code snippets right into .pyc
    * compare - function ompare bytecode among different sources and produce neat table with stats of the used opcodes
    * main - the main function of the script
"""

import dis, sys
import py_compile
from contextlib import redirect_stdout
from tempfile import NamedTemporaryFile

def expand_bytecode(bytecode):
    """
    Function find and extends bytecode result
    :param bytecode: bytecode
    :return: list with instructions
    """
    result = []
    for instruction in bytecode:
        if str(type(instruction.argval)) == "<class 'code'>":
            result += expand_bytecode(dis.Bytecode(instruction.argval))
        else:
            result.append(instruction)

    return result

def compile():
    """
    Function produce (compile) .py files or code snippets right into .pyc
    :param None: None 
    :return: compiled files
    """
    for i in sys.argv[3:]:
        if sys.argv[2] == "-s":
            with NamedTemporaryFile("w", delete=True) as tmp:
                tmp.write(i)
                tmp.seek(0)
                py_compile.compile(tmp.name, cfile= "out.pyc")
        elif sys.argv[2] == "-py":
            try:
                py_compile.compile(i, cfile=i+"c")
            except Exception as e:
                print(f"We are skipping...{i}")

def compare():
    """
    Function ompare bytecode among different sources and 
    produce neat table with stats of the used opcodes
    :param None: None
    :return: comparison table
    """
    arg_arr = sys.argv[2:]
    file2res = {} # source code name to dictionary with instructions
    all_instructions = set()
    for i in range(len(arg_arr)):
        if arg_arr[i] == "-py":
            with open(arg_arr[i+1], 'r') as f:
                source = f.read()

            bc = dis.Bytecode(source)
            res = expand_bytecode(bc)
            
            func2opcodes = {} # dictionary instrucition : num occurances
            opcodes = []
            
            for instruction in res:
                opcodes.append(instruction.opname)
                # get all instruction that appear in all bytecode files
                all_instructions.add(instruction.opname)

            func2opcodes = dict((i, opcodes.count(i)) for i in opcodes)
            # add source code name : dictionary with related instruction
            file2res.update({arg_arr[i+1] : func2opcodes})
            
    # Working on tabl formating
    table_headers = ["Instructions |"]
    list_srccode = list(map(lambda s: s+'|', list(filter(lambda x: x != '-py', arg_arr))))
    table_headers += list_srccode

    header = "{name[0]:18}"
    for i in range(len(list_srccode)):
        new = "{name[" + str(i+1)+ "]:6}"
        header += new 
    # put table to file
    with open('result.txt', 'a') as f:
        with redirect_stdout(f):    
            print(header.format(name=table_headers))
            for ins in all_instructions:
                names = []
                names.append(ins)
                file_names = file2res.keys()
                for i in file_names:
                    instructions_dict = file2res.get(i)
                    num_occurance = instructions_dict.get(ins)
                    if num_occurance == None:
                        num_occurance = 0
                    names.append(num_occurance)
                print(header.format(name=names))
        
if __name__ == "__main__":
    # Main logic for 4&5 Task
    if sys.argv[1] == "compile":
        compile()
    elif sys.argv[1] == "compare":
        compare()
    else:
        print("Error in ordinal arguments for the script")