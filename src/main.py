import random
from task1 import best_decorator
from task2 import best_decorator_v2
from math import sqrt
from cmath import sqrt as csqrt

@best_decorator_v2
def pascal_triangle(num):
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

@best_decorator
def double_list(list):
    """
    Function including lambda for double each element in the list
    :param list: list for double elemt
    :return: Doubled list
    """
    return list(map(lambda elem: elem * 2 , list))

@best_decorator
def quad_solver(a=1,b=4, c=2):
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

@best_decorator
def find_polin(str_list=["php", "w3wp", "Python", "abcd", "Java"]):
    """
    Function find and return list of polindroms from the given string list with words
    :param list: string list with words
    :return: list with polindromes
    """
    return list(filter(lambda elem: (elem == "".join(reversed(elem))), str_list))

@best_decorator
def func():
    print("I am ready to Start")
    result = 0
    n =  random.randint(10,751)
    for i in range(n):
        result += (i**2)
        
@best_decorator
def funx(n=2, m=5):
    print("I am ready to do serious stuff")
    max_val = float('-inf')
    n =  random.randint(10,751)
    res = [pow(i,2) for i in range(n)]
    for i in res:
        if i > max_val: 
            max_val = i

if __name__ == "__main__":
    pass