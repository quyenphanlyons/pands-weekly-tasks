# Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
# sqrt(n) = S
# let's call x the guess valur of S
# f(x) = x**2 - n
# f'(x) = 2x
# x(n+1) = x(n) - f(x) / f'(x) which is 



# Enter a number as input
n = float(input("Please enter a positive floating-point number: "))

while n <= 0:
    n = float(input("Please enter only positive floating-point number: "))

# Enter a guess of square root of n
x = float(input("Please enter the guess of square root of {} :".format(n) ))

# Calculate x1: the new value of square root of n
x1 = x - ((pow(x, 2) - n))/(2*x)

# Calculate the difference of x1 and x
dif = abs(x1-x)

# Lets set the tolerance at 0.00001
# If the difference is greater than 0.00001: set a new x = x1 and calculate the new x1 and new dif
while dif > 0.00001:
    x = x1
    x1 = x - ((x**2 - n))/(2*x)
    dif = abs(x1-x)
else: 
    print ("Square root of {} is {} :".format(n,x1))






