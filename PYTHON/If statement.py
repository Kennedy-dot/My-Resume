#Simple Example
#let's try a guess-a-number program. The computer picks a random number,the player tries...
# to guess, and the program tells them if they are correct.
#To see if the player's guess is correct, we need something new, called an if statement.

from random import randint

num = randint(1,10)
guess = eval(input('Enter your Guess: '))
if guess==num:
    print('You got it! ')
else:
    print('Sorry. The number is ', num)


#CONDITIONAL OPERATORS
#The comparison operators are ==,>,<,>=,<=, and !=.

#There are three additional operators used to construct more complicated conditions:
# and,or, and not.

grade = eval(input('Enter your grade: '))
if grade>=80 and grade<90:
    print('Your grade is a B. ')
score = eval(input('Enter your score'))
time = eval(input('Enter the time: '))
if score>1000 or time>20:
    print('game over. ')
