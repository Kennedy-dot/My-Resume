grade = eval(input('Enter your score: '))

if grade>=90:
    print('A')
elif grade>=80:
    print('B')
elif grade>=70:
    print('C')
elif grade>=60:
    print('D')
else:
    print('F')

#With the separate if statements, each condition is checked regardless of whether it really needs to be.
#Using elif, as soon as we find where the score matches, we stop checking conditions and skip all the way to the end of the whole block of statement.
