import random
from cmath import sqrt as csqrt

from task1 import best_decorator
from task2 import best_decorator_v2
from task3 import BestDecor
from task4 import best_decorator_v4, BestDecor4

def pascal_triangle(num=5):
    """
    Pacal triangle approach with O(N^2) approach with O(1) extra space
    (More interesting solutions here: https://www.codesdope.com/blog/article/pascal-triangle-algorithm/)
    :param num: amout of pascal triangle lines (depth)  
    """
    for n in range(1, num + 1):  
        column = 1   
        for k in range(1, n + 1):   
            # value of first column is always 1  
            print(column, end = " ")  
            column = int(column * (n - k) / k)  
        print("") 

def double_list(list_num=[1, 2, 3, 4, 5]):
    """
    Function including lambda for double each element in the list
    :param list: list for double elemt
    :return: Doubled list
    """
    print(list(map(lambda elem: elem * 2 , list_num)))

def quad_solver(a=1,b=4,c=2):
    """
    The function solve quad equation also with complex space
    :param a: arg in x^2
    :param b: arg in x
    :param c: free component
    """
    # calculating  the discriminant
    dis = (b**2) - (4 * a*c)
    # find two results
    root_1 = (-b-csqrt(dis))/(2 * a)
    root_2 = (-b + csqrt(dis))/(2 * a)
    print("Solution for equation: ({0})x^2+({1})x+({2})\nRoots:\n{3}\n{4}".format(a, b, c, root_1, root_2))

def find_polin(str_list=["php", "w3wp", "Python", "abcd", "Java"]):
    """
    Function find and return list of polindroms from the given string list with words
    :param list: string list with words
    :return: list with polindromes
    """
    print(list(filter(lambda elem: (elem == "".join(reversed(elem))), str_list)))

def func():
    print("I am ready to Start")
    result = 0
    n =  random.randint(10,751)
    for i in range(n):
        result += (i**2)
      
def funx(n=2, m=5):
    print("I am ready to do serious stuff")
    max_val = float('-inf')
    n =  random.randint(10,751)
    res = [pow(i,2) for i in range(n)]
    for i in res:
        if i > max_val: 
            max_val = i

def test_case_task_1():
    a = best_decorator(funx)
    b = best_decorator(func)

    a()
    b()
    a()

def test_case_task_2():
    pt = best_decorator_v2(pascal_triangle)
    qs = best_decorator_v2(quad_solver)

    pt(5)
    qs()

def test_case_task_3():
    # list of executable functions
    func2exec = [pascal_triangle, quad_solver, double_list, find_polin]
    func2time = {}
    for i in range(len(func2exec)):
        # instance
        func = BestDecor(func2exec[i])
        #execute
        func()
        func2time.update({func2exec[i] : func.executed_time})
    # sort by time execution the results of function
    sorted_exec = sorted(func2time.items(), key = lambda func_time: func_time[1])
    print("{0:15} {1:} {2:15}".format("Function", "|RANK", "|TIME ELAPSED"))
    rank_order = 0
    for func, func_time in (sorted_exec):
        rank_order += 1
        print('{0:15} {1:} {2:15}s'.format(func.__name__, rank_order, round(func_time,8)))

def func_error():
    raise Exception('Python!')

def test_case_task_4():
    a = best_decorator_v4(func_error)
    a()

if __name__ == "__main__":
    # Test case for Task #1
    test_case_task_1()
    # Test case for Task #2
    test_case_task_2()
    # Test case for Task #3
    test_case_task_3()
    # Test case for Task #4
    test_case_task_4()