# Exception handling when using 'input' function to take data from user input and work with that,

a = input('type a number:')
b = input('type another number:')
a = int(a)
b = int(b)

print(a/b)

# works fine with whole numbers but an error is created if the user decided to enter a zero.

#########################################################################################
# same equation but with the built in function 'try' and 'except' to test the formula first.
# if the error message stated in the except clause would be the result the text below prints.

try:

    a = input('type a number:')
    b = input('type another number:')
    a = int(a)
    b = int(b)

    print(a/b)
except (ZeroDivisionError, ValueError):
    print('Invalid input. Sorry, that will not work!')

    
# used multiple except parameters to account for user typing a string (e.g million) instead of an interger in addition to using a 0.

