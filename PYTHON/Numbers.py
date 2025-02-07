#Math operators

#Exponentiation..python uses ** for exponentiation.


#Integer division. The intager division operator,//,requires some explanation.
#for positive numbers it behaves like ordinary division except that it throws away thedecimal part of the result.
#eg 8/5=1.6 while 8//5=1

#Modulo(Remainder) %
#returns the remainder from a division.
#eg 18%7=4 because 4 is the remainder when 18 is divided by7.


#Order of operations
#Exponentiation gets done first,followed by multiplication and division(including// and %), and addition and subtraction come last.

#Random numbers
#If we want to use something from a module we have to first import it.
#Here we want one function called randint,that we will need from the random module.
#To load this functino,we use the following statement:
#from random import randint
#Using randint is simple: randint(a,b) will return a random integer between a and b including both a and b.
#NB: randint includes the right endpoint b unlike the range function.
from random import randint
x = randint(1, 10)
print('A random number between 1 and 10: ', x)
#The random number will be different every time we run program.


#Math function
