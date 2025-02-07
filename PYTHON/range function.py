#The value we put in the range function determines how many times we will loop.
#The way range works is it produces a list of numbers from zero to the value minus one.
#If we want the list of values to start at a value other than 0,we can do that by specifying the starting value.
#The statement range(1,5) will produce the list 1,2,3,4.
#Another thing we can do is to get the list of values to go up by more than one at a time
#To do this, we can specify an optional step as the third argument.
#The statemnt range(1,10,2) will step through the list by two's,producing 1,3,5,7,9.

#Here is an example program that counts down from 5 and then prints a message.
for i in range(5,0,-1) :
    print(i, end='')#The end=' ' just keeps everything on the same line.
print('Blast off!!')


#The program below prints a rectangle of stars that is 4 rows tall and 6 rows wide.
for i in range(4):
    print('*'*6)


#suppose we want to make a triangle instead.The key is to change the 6 to i+1.
#Each time through the loop the program will now print i+1 stars instead of 6 stars.
for i in range(4):
    print('*'*(i+1))

#Write a program that prints your name 100 times.
for i in range(100):
    print('KENNEDY MUSYOKA')


