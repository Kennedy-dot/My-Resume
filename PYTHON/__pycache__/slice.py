# A slice is used to pick out part of a string. 
#It behaves like a combination of indexing and the range function
#eg'
# index 0 1 2 3 4 5 6 7 8 9
#letters a b c d e f g h i j
# s[2:5] result cde characters at indices 2 3 4
#s[ :5] abcde first five chsrscters.
# s[5: ] fghij characters from index 5 to the end.
# s[-2: ] ij last two characters.
# s[ : ] all letters entire string
# s[1:7:2] bdf characters from index 1 to 6, by twos
# s[ : :-1] jihgfedcba a negative step reverses the string.

# The basic structure is...
#  string name[starting location:ending location+1]
# we can leave either the starting or ending locations blank.
s = "a,b,c,d"
print(s[2:])