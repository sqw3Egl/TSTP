# write a function that takes three required parameters and two optional parameters.

def add_mult(a, b, c, x=100, y=1000):
    return a + b + c * x * y

result = add_mult(10, 15, 25)
print(result)
