#Strings are a data type in Python dealing with text.
#A String is created by enclosing text in quotes.using single quotes or double quotes.
#A triple-quote can be used for multi-line strings.
# When getting numerical inpit we use an eval statement with the input statement,
# but when getting text, we do not use eval.
num = eval(input('Enter a number: '))
string = input('Enter a string: ')
# Empty string '' is the string equivalent of the number 0.it is a string with nothing in it.

#To get the LENGTH  of a string(how many characters it has), use the built-in function len.
#eg, 
len('Kennedy')

# Concatenation and repetition
#Concatenation(operator +) combines two strings.
# (*) repeats a string a certain number of times.
# eg, 'AB'+'cd' u get 'ABcd'
#'Hi' * 4 you get 'HiHiHiHi'

# i f we want to print a long row of dashes, we can do the following
print('-'*75)