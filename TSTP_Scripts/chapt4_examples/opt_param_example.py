# optional parameters - example
# syntax: [function_name]([parameter_name]=[parameter_value])

def f(x=2):
    return x**x

print(f()) # with no value the default (2) is used.
print(f(4)) # with a value the default is ignored and (4 in this example) is used.


#################################################################################

# required parameters MUST been defined before optional parameters

def add_it(x, y=10):
    return x + y

result = add_it(2)
print(result)


##################################################################################

#SCOPE of variables: Global variables defined outside of a function can be read/write from anywhere in the program. Local variables defined within a function can only
# be written to from within the defined variable.


x = 1  #Variables defined outside of the function GLOBAL VARIABLES.
y = 2
z = 3

def f():
    print(x)
    print(y)
    print(z)

f()



def f():
    x = 1  #Variables defined within a function LOCAL VARIABLES
    y = 2
    z = 3
    print(x)
    print(y)
    print(z)

f()

#########################################################################################

#example of writing a global function INSIDE a variable



x = 100

def f():
    global x
    x += 1
    print(x)

f()





