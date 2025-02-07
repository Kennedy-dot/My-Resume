#FLAG VARIABLES
#A flag variable can be used to let one part of your program know when something happens in another part of the program.
#Here is an example that determines if a number is prime.

num = eval(input('Enter number: '))

flag = 0
for i in range(2,num):
    if num%i == 0:
        flag = 1

if flag == 1:
    print('Not prime')
else:
    print('prime')

#A Number is prime if it has no divisors other than 1 and itself.
#The way the program works is flag starts off at 0.
#We then loop from 2 to num-1.if one of those values turns out to be a divisor, then flag gets set to 1.
#Once the loop is finished, we check to see if the flag got set or not.
#If it did, we know there was a divisor, and num isn't prime.
#Otherwise, the number must be prime.