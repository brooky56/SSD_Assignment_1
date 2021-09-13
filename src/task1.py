import time
from contextlib import redirect_stdout

def best_decorator(func):
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
        with open('stdout.txt', 'a') as f:
            with redirect_stdout(f):
                func(*args, **kargs)
        executed_time = time.time() - start_time
        print("{0} call {1} executed in {2} sec".format(func.__name__ ,wrapper.counter, round(executed_time, 4)))
    wrapper.counter = 0
    return wrapper