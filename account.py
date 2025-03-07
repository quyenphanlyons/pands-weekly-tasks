#Task 3
#Please enter an 10 digit account number
#only display the last 4 characters (with the other other characters replaced with Xs)

#TO DO: fix the number of account to 10

account = int(input('Please enter 10 digit of an account number: ')) # variable account can only contains numbers
account_str = str(account)
display = account_str.replace(account_str[0:6],'XXXXXX')
print(display)

