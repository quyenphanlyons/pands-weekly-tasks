# Task 4
# Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# Have the program end if the current value is one.

# -------------------

# Ask user to enter a positive number
x = int(input("Enter a positive number: "))

# Ask user to enter a number until receiving a positive number
while x <= 0: 
    x = int(input("Please enter only positive number: "))

# Create a list contains the value entered
list=[x]

# if first value of x is 1, the calculation of the next value processes anyway  
# if x is an even number    
if x%2==0:  
    # divide it by two
    x = int(x/2)
    #Add the new value of x in the existing list
    list.append(x) 
# if x is an odd number
else: 
    # multiply it by three and add one
    x = int(x*3+1)
    #Add the new value of x in the existing list
    list.append(x) 

# after the second value is added in the list apply the condition while until the value of x=1
while x!=1: 
    if x%2==0:        
        x = int(x/2)
        list.append(x)
    else: 
        x = int(x*3+1)
        list.append(x)

print(*list)
