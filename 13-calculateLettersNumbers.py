# Question 13
# Level 2

'''
Question: Write a program that accepts a sentence and calculate the 
number of letters and digits. Suppose the following input is supplied 
to the program: hello world! 123 Then, the output should be: 
    #LETTERS 10 DIGITS 3

Hints: In case of input data being supplied to the question, 
it should be assumed to be a console input.
'''

# Solution:

inputString = input("Enter a string consisting of letters and numbers: ")
dict = {"DIGITS":0, "LETTERS":0}
for i in inputString:
    print(i)
    if i.isdigit():
        dict["DIGITS"] += 1
    elif i.isalpha():
        dict["LETTERS"] += 1
    else:
        pass

print("LETTERS", dict["LETTERS"])
print("DIGITS", dict["DIGITS"])