# Task 3
# Write a python program called accounts.py that reads in a 10 character account number and 
# outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).

# -------------------

# Ask user to enter an account number by using int()
account = int(input('Please enter 10 digit of an account number: ')) # variable account can only contains numbers

# Turn the account number entered into string and store it in account_str
account_str = str(account)
# n: the number of characters in variable account_str 
n = len(account_str)
# Only display the account number when it contains 10 digits (when n=correctlen)
# If else send an error message
if n == 10:
    # Replace the first 6 characters of variable account_str by XXXXXX and store it in display
    display = account_str.replace(account_str[0:6],'XXXXXX') 
    print("User's account number is {}".format(display))
else: 
    account = int(input('Account number must be exactly 10 digits. Please enter again an account number: '))