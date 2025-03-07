#the user to input any positive integer and outputs the successive values of the following calculation.
#At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.

x = int(input("Enter a positive number: "))
list=[x]

while x!=1:
    if x%2==0:        
        x = int(x/2)
        list.append(x)
    else: 
        x = int(x*3+1)
        list.append(x)

print(list)





