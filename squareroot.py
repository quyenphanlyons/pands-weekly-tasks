# Task 6
# Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
# You should create a function called <tt>sqrt</tt> that does this.
# I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).
# This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods). 
# I suggest that you look at the newton method at estimating square roots. 
# This is a more difficult task than some of the others, but will be marked equally, so only do as much work on this as you feel comfortable.

# -------------------


# Square roots estimation - Newton method
# let's suppose S is the square root of n
# sqrt(n) = S
# let's call x the guess valur of S
# f(x) = x**2 - n
# f'(x) = 2x
# x(n+1) = x(n) - f(x) / f'(x) 


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
    # Round the output to the 2nd decimal place
    return round(x1,2)

# enter the value to calculate its square root: for example 14.5
n=14.5

print(f"Square root of {n} is {sqr(n,x=1)}")