#input buuilt-in function acccepts user input

age = input("Enter your age:")
int_age = int(age)

if int_age < 21:
    print("You are young!")
else:
    print("Wow, you are old!")
    
# input function colects data from a user as str data type, so need to use
# 'int' to change the user input into int datat type.

################################################################################

# even though a return value hasn't been defined, it still tests the if statement.

def even_odd(x):
    if x % 2 == 0:
        print("even")
    else:
        print("odd")


even_odd(2)
even_odd(3)

################################################################################

# calling a function multiple times to reduce the need to repeat the same code over and over

def even_odd():
    n = input("type a number:")
    n = int(n)
    if n % 2 == 0:
        print("n is even.")
    else:
        print("n is odd.")


even_odd()  #no parameter used in the function as input from user is tested. thsi calls the function 3 times. 
even_odd()
even_odd()
        
