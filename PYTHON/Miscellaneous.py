#COUNTING
#Very often we want our programs to count how many times something happens.
#EXAMPLE...This program gets 10 numbers from the user and counts how many of those numbers are greater than 10.

count = 0 #We set it to 0 to indicate that at the start of the program no numbers greater than 10 have been found.
for i in range(10):
    num = eval(input('Enter a number: '))
    if num>10:
        count=count+1
print('There are', count, 'numbers greater than 10. ')

#Think of the count variable as if we are keeping a tally on a piece of paper.
#Every time we get a number larger than 10,we add 1 to our tally.
#In the program,this is accomplished b the line count=count+1.
#Counting is an extremely common thing.The two things involved are:
# 1.count=0--Start the count at 0.
# count=count+1--Increase the count by 1.

#EXAMPLE 2 This modification of the previous example counts how many of the numbers the user enters are greater than 10...
#and how many are equal to 0.To count two things we use two count variable.

count1 = 0
count2 = 0
for i in range(10):
    num = eval(input('Enter a number: '))
    if num>10:
        count1=count1+1
    if num==0:
        count2=count2+1
print('There are', count1, 'numbers greater than 10. ')
print('There are', count2, 'zeros.' )

#EXAMPLE 3 This program counts how many of the squares from 1^2 to 100^2 end in a 4.
count = 0
for i in range(1,101):#loops through the numbers 1 through 100.
    if (i**2)%10==4:
        count = count + 1
print(count)
#To check if a number ends in 4, a nice mathematical trick is to check if it leaves a remainder of 4 when divided by 10.The module operator is,%,is used to get the remainder.
