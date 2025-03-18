#Task 3
#Please enter an 10 digit account number
#only display the last 4 characters (with the other other characters replaced with Xs)

account = int(input('Please enter 10 digit of an account number: ')) # variable account can only contains numbers
account_str = str(account) # create variable account_str type string from variable account
display = account_str.replace(account_str[0:6],'XXXXXX') # create variable displace from variable account_str by replacing the first 6 character of variable account_str by XXXXXX
n = len(account_str) # n is the number of characters in variable account_str 
correctlen=10 # correctlen is fixed at 10

#Only display the account number when it contains 10 digits (when n=correctlen)
#If else send an error message

if n == correctlen:
    print("User's account number is {}".format(display))
else: 
    print('This is not a valid number')
    account = int(input('Please enter 10 digit of an account number: '))


