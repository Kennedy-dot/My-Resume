# The + operator can be used to build up a string, piece by piece,analogously to the way we built up controls and sums.
#Here is an example that repeatedly asks the user to enter a letter and builds up a string consisting of only the vowels that the user entered.
s = ''
for i in range(10):
    t = input('Enter a letter: ')
    if t=='a' or t=='e' or t=='i' or t=='o' or t=='u':#Can be replaced with in operator
        # if t in 'aeiou':
        s = s + t
print(s)
#This technique is very useful.
