#RANDOM NUMBERS
#Python comes with a module,called random, that allows us to use random numbers in our programs.
#if we want to use something from module we have to first import it-that is,tell Python we want to use it.
#At this point, there is only one function,called randint,that we will need from the random module
# from random import randint
# randint(a,b) will return a random integer between a and b including both a and b.

from random import randint
x = randint(1,10)
print('A random number between 1 and 10: ', x)

#MATH FUNCTIONS
#The math module Python has a module called math that contains familiar math functions,
# including sin,cos,tan,exp,log,log10,factorial,sqrt,floor, and ceil.

from math import sin, pi
print('Pi is roughly', pi)
print('sin(90) =', sin(90))

#Built-in math functions
#these are abs(absolute value) and round that are available without importing the mat module.

print(abs(-4.3))
print(round(3.336, 2))
print(round(345.2, -1))

#GETTING HELP FROM PYTHON
#There is documentation built into Python.
#To get help on the math module,for example,go to the Python shell and type the following two lines:
# >>> import math
# >>> dir(math)
#To get help on a specific function, say the floor function,you can type help(math.floor)
