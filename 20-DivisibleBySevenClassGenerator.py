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

for number in divisibleBySeven.bySeven(100):
    print(number)
