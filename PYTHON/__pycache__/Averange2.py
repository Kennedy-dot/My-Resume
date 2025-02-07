#This program that will ask the user for 10 numbers and then computes their average.
s = 0
for i in range(10):
    num = eval(input('Enter a number: '))
    s = s + num
print('The average is', s/10)

#A common use for summing is keeping score in a game.
#Near the beginning of the game we would set the score variable equal to 0.
#Then when we want to add to the score we would do something like below
# score = score + 10
score = 0
for i in range(5):
    score = eval(input('Enter a score: '))
    score = score + 10
print("The score is", score)
##SWAPPING
# x,y = y,x