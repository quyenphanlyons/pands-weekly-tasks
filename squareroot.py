# Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
# sqrt(n) = S
# let's call x the guess valur of S
# f(x) = x**2 - n
# f'(x) = 2x
# x(n+1) = x(n) - f(x) / f'(x) which is 


# the function squareroot id defined with 2 parameters: n and x.
# n is the number whose square root we need to calculate
# x is a guess of square root of n, x will be 1 by default if user doesn't enter a value for x
def sqr(n,x=1):

    # Calculate x1: the new value of square root of n
    x1 = x - ((pow(x, 2) - n))/(2*x)
    # Calculate the difference of x1 and x
    dif = abs(x1-x)
    # n must be positive, if else user will receive an error message
    if n>0: 
        # Lets set the tolerance at 0.00001
        # If the difference is greater than 0.00001: set a new x = x1 and calculate the new x1 and new dif
        while dif > 0.00001:
            x = x1
            x1 = x - ((x**2 - n))/(2*x)
            dif = abs(x1-x)
    else: 
        return "Error: The number must be positive!"
    return x1

