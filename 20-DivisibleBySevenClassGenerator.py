# Question 20
# Level 3

'''
Question: Define a class with a generator which can iterate the numbers, 
which are divisible by 7, between a given range 0 and n.

Hints: Consider use yield
'''

# Solution:

class DivisibleBySeven:
    def bySeven(self, n):
        for number in range(0,n):
            if number%7==0:
                yield number

divisibleBySeven = DivisibleBySeven()

# for number in divisibleBySeven.bySeven(100):
    # print(number)

'''
Question 68
Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.

Example: If the following n is given as input to the program:

10

Then, the output of the program should be:

0,2,4,6,8,10

Hints: Use yield to produce the next value in generator.

In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:

'''

def EvenGenerator(n):
    i = 0
    while i<=n:
        if i%2==0:
            yield i
        i+=1

n=int(input("Enter a number: "))
values = []
for i in EvenGenerator(n):
    values.append(str(i))

# print(",".join(values))


'''
Question 69
Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

Example: If the following n is given as input to the program:

100

Then, the output of the program should be:

0,35,70

Hints: Use yield to produce the next value in generator.

In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:

'''

def NumGenerator(n):
    for i in range(n+1):
        if i%5==0 and i%7==0:
            yield i

n=int(input("Enter any number:"))
values = []
for i in NumGenerator(n):
    values.append(str(i))

# print(",".join(values))

li = [2,4,6,8]
for i in li:
    assert i%2==0, "{} is not an even number".format(i)
print("All numbers are even")


expression = input("Enter an expression:")
print(eval(expression))

