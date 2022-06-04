"""
14. What is the problem with the following code?
answer : 'OSError', superclass of the exception class 'FileNotFoundError', has already been caught
"""


def f():
    pass


try:
    f()  # Function f can raise an exception
except OSError:
    print(1)
except FileNotFoundError:
    print(2)
""" its better :
except FileNotFoundError:
    print(2)
except OSError:
    print(1)
"""
