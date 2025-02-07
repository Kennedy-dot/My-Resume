#FOR LOOP
#There are several ways to repeat things in python,most common of which is the for loop.
#Following program will print Hello ten times.
for i in range(10):
    print('Hello')
    #Structure of a for loop is as follows;
    #for variable name in range(number of times to repeat):
        #statement to be repeated
for i in range(5):
    print('I LOVE YOU GOD')    

#The program below asks the user for a number and prints its square, then asks for another number and prints its square, etc. It does this three times and then prints that the loop is done.
for i in range (3):
    num = eval(input('Enter a number: '))
    print('The square of your number is', num*num)
print('The loop is now done.')    

#The program below will print A, then B, then it will alternate C's and D's five times and then finish with the letter E once.
print('A')
print('B')
for i in range (5):
    print('C')
    print('D')
print('E')    

#If we wanted the above program to print five C's followed by five D's, instead of alternating C's and D's, we could do the following:
print('A')
print('B')
for i in range(5):
    print('C')
for i in range(5):
    print('D')
print('E')

