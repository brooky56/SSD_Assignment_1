"""Opcodes printing

Takes .py files and yield opcodes (and their arguments) for ordinary python programs. 

This file can also be imported as a module and contains the following
functions:

    * expand_bytecode - function find and extends bytecode result
    * bc_print - function print instructions names and human readable description of operation argument 
    * main - the main function of the script
"""

import marshal
import dis, sys

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

def bc_print():
    """
    Function print instructions names and human readable description of operation argument
    :return: None
    """
    for i in sys.argv[2:]:
        source = None
        if sys.argv[1] == "-py":
            with open(i, 'r') as f:
                source = f.read()
        elif sys.argv[1] == "-pyc":
            header_size = 12
            with open(i, 'rb') as f:
                f.seek(header_size)
                source = marshal.load(f)
        elif sys.argv[1] == "-s":
            source = i
        else:
            print("Error")
            return

        bc = dis.Bytecode(source)

        res = expand_bytecode(bc)
        for instruction in res:
            print(f'{instruction.opname}\t {instruction.argrepr}')
        print()
        print()

if __name__ == "__main__":
    # main execution logic for Tasks 2&3
    bc_print()
