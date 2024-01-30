# Question 14
# Level 2

'''
Question: Write a program that accepts a sentence and calculate the 
number of upper case letters and lower case letters. 
Suppose the following input is supplied to the program: 
Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9

Hints: In case of input data being supplied to the question, 
it should be assumed to be a console input.
'''

# Solution:

inputString = input("Enter a string consisting of lower and upper case letters: ")
dict = {"UPPER":0, "LOWER":0}
for i in inputString:
    if i.isupper():
        dict["UPPER"] += 1
    elif i.islower():
        dict["LOWER"] += 1
    else:
        pass

print("UPPER", dict["UPPER"])
print("LOWER", dict["LOWER"])