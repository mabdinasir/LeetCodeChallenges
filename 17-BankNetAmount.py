# Question 17
# Level 2

'''
Question: Write a program that computes the net amount of a bank account 
based a transaction log from console input. The transaction log format is 
shown as following: D 100 W 200

D means deposit while W means withdrawal. Suppose the following input 
is supplied to the program: D 300 D 300 W 200 D 100 
Then, the output should be: 500

Hints: In case of input data being supplied to the question, 
it should be assumed to be a console input.
'''

# Solution:

netAmount = 0

inputTransaction = input("Enter a transaction: ") # D 300 D 300 W 200 D 100

values = inputTransaction.split()

for i in range(0, len(values), 2):
    operation = values[i]
    amount= values[i+1]
    if amount:
        amount = int(amount)
        if operation == "D":
            netAmount += amount
        elif operation == "W":
            netAmount -= amount
        else:
            pass
print("Net amount:", netAmount)
