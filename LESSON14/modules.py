

from math import pi # only imports pi from math module
import sys
import random as rdm # can create alias (e.g. rdm =random)
from enum import Enum # importing a part of the module enum
import kansas # custome module


print(pi)

for item in dir(rdm):
    print(item)

# Use Python Documentation online to learn more about the functions in the modules.

print(kansas.capital)
kansas.randomfunfact()

print(__name__) # returns __main__ b/c this is the file being ran
print(kansas.__name__)
