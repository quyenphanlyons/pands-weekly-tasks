# Task 2
# Write a program called bank.py 
# The program should:
# Prompt the user and read in two money amounts (in cent)
# Add the two amounts
# Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 

# -------------------


# Ask user to put 2 amounts in cent
a1,a2=map(int, input("Please enter two amounts in cent: ").split()) 
#input: taking value
#split: for taking multi inputs
#map: converts each input into the defined datatype which is integer
sum=(a1+a2)/100
print('€',sum) #print out this sum with the currency in front
