#Task 3
#Please enter an 10 digit account number
#only display the last 4 characters (with the other other characters replaced with Xs)

#TO DO: fix the number of account to 10 & only contains number

account = str(input('Please enter 10 digit of an account number: '))
display = account.replace(account[0:6],'XXXXXX')
print(display)

