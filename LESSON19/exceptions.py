# Error handling
# Wrap what you are trying to do in a try block with at least one except.
class JustNotCoolError(Exception):
    pass

x = 2
try:
    raise JustNotCoolError("This just isn't cool, man.")
    # raise Exception("I'm a custom exception!") # Usually the exceptions are named by what they will be
    # print(x / 0)
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed.")
except NameError:
    print("NameError means something is probably undefined.")
except ZeroDivisionError:
    print("Please do not divide by zero.")
except Exception as error:
    print(error)
else: # Will happen only if no erros occur.
    print('No errors!')
finally: # Will happen wether there are exceptions or not.
    print("I'm going to print with or without an error.")