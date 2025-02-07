#This program will add up the numbers from 1 to 100.
#The way this works is that each time we encounter a new number, we add it to our running total, s.
s = 0
for i in range(1,101):
    s = s + i
print('The sum is', s)