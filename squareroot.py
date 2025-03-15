# Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
# sqrt(n) = S
# let's call x the guess valur of S
# f(x) = x**2 - number
# f'(x) = 2x
# x(n+1) = x(n) - f(x) / f'(x) which is 


n = int(input("Please enter a positive number: "))

x = input("Please enter the guess of square root of {} :".format(number) )

x1 = x - ((x**2 - n))/(2*x)

tolerance = 0.00001




