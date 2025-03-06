#Ask user to put 2 amounts in cent
a1,a2=map(int, input("Please enter two amounts in cent: ").split()) 
#input: taking value
#split: for taking multi inputs
#map: converts each input into the defined datatype
sum=(a1+a2)/100
print('€',sum) #print out this sum with the currency in front
