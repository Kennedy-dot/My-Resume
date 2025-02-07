#Program that generates 10000 random numbers between 1 and 100 and counts how many of them are multiple of 12.
#Because we are using random numbers,the first line of the program should import the random module.
#we will require a for loop to run 10000 times.
#inside the loop, we will need to generate a random number, check to see if it is divisable by 12, and if so, add 1 to the count.
#Since we are counting, we will also need to set the count equal to 0 before we start counting.
#To check divisibility by 12, we use the modulo, %, operator.

from random import randint
count = 0
for i in range(10000):
    num = randint(1, 100)
    if num%12==0:
        count=count+1

print('Number of multiples of 12:', count)  