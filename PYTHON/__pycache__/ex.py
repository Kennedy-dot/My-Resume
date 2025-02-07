#In this section we will look in depth at some simple programs and try to understand how they work.

#The following program prints Hello a random number of times between 5 and 25.

from random import randint # import statement.

rand_num = randint(5,25) # generates a arandom number btn 5 and 25
for i in range (rand_num):# to repeat something a specified number of times, we use a for loop.
    #To repeat something a arandom number of times, we can use range(rand_num),where rand_num is a variable holding a random number.
    # Although if we want, we can skip the variable and put the randint statement directly in the range function 
    print('Hello')

from random import randint

for i in range(randint(5,25)):
    print('Hello')