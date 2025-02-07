#To find largest and smallest value in a series of values.
#Here is an example where we ask the user to enter ten positive numbers and then we print the largest one.

largest = eval(input('Enter a positive number: '))
for i in range(9):
    num = eval(input('Enter a positive number: '))
    if num>largest:
        largest=num
print('Largest number:', largest)

#The key here is the variable largest that keeps track of the largest number found so far.
#We start by setting it equal to the user's first number.
#Then, every time we get a new number from the user, we check to see if the users number is larger than the current largest value(which is stored in largest).
#If it is, then we set largest equa to the users number.
#IF instead we want the smallest value, we change > to < and also rename the variable largest to smallest.
