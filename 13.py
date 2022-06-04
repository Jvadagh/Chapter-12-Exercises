"""
13. What is the problem with the following code?
answer : 'Exception', superclass of the exception class 'ValueError', has already been caught
"""

def f():
    pass


try:
    f()  # Function f can raise an exception
except Exception:
    print(1)
except ValueError:
    print(2)
