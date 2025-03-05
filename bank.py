#Ask user to put 2 amounts in cent
a1,a2=input("Enter 2 amounts in cent: ").split() #function input source geeksforgeeks.org
a1=int(a1) #a1 is a number
a2=int(a2) #a2 is a number
sum=a1+a2
print('€',sum) #print out this sum with the currency in front
