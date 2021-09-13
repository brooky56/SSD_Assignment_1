import time
from io import StringIO
from contextlib import redirect_stdout
from inspect import signature, getsource

def best_decorator_v2(func):
    """
    Feat.1 Best decorator wrappes and add additional logic to the wrapped functions
    Feat.2 Redirect all stdout to stdout.txt file - all output of fucntion calling find there
    """
    def wrapper(*args, **kargs):
        """
        The solution is to use *args and **kwargs in the inner wrapper function. 
        Then it will accept an arbitrary number of positional and keyword arguments
        :param args: positional arguments
        :param kargs: keyword argumants (set)
        """
        wrapper.counter +=1
        start_time = time.time()
        f = StringIO()
        with redirect_stdout(f):
            func(*args, **kargs)
        executed_time = time.time() - start_time
        print("{0} call {1} executed in {2} sec\n".format(func.__name__ ,wrapper.counter, round(executed_time, 4)))
        print(
            """
            Name: {0}\n
            Type: {1}\n
            Sign: {2}\n
            Args: positional {3}\n
                  key=worded {4}
            Doc: {5}\n
            Source: {6}\n
            Output: {7}
        """.format(func.__name__, type(func), signature(func), args, kargs, func.__doc__, getsource(func), f.getvalue()))
    wrapper.counter = 0
    return wrapper