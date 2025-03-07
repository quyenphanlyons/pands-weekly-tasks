#Task 3
#Please enter an 10 digit account number
#only display the last 4 characters (with the other other characters replaced with Xs)

#TO DO: fix the number of account to 10

account = int(input('Please enter 10 digit of an account number: ')) # variable account can only contains numbers
account_str = str(account)
n = len(account_str)
if n != 10:
    print('An account number must contains 10 digits!')
else: display = account_str.replace(account_str[0:6],'XXXXXX')
print("User's account number is {}".format(display))