# So far, we have only heard of Python's powers. Now, we will witness them!

# Powers or exponents in Python can be calculated using the built-in power function. Call the power function  as shown below:

# >>> pow(a,b) 
# or

# >>> a**b
# It's also possible to calculate a^b mod m.

# >>> pow(a,b,m)  
# This is very helpful in computations where you have to print the resultant % mod.

# Note: Here, a and b can be floats or negatives, but, if a third argument is present, b cannot be negative.

# Note: Python has a math module that has its own pow(). It takes two arguments and returns a float. It is uncommon to use math.pow().

# Task
# You are given three integers: a, b, and m. Print two lines.
# On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).

# Input Format
# The first line contains , the second line contains , and the third line contains .

# Solution:
a = int(input())
b = int(input())
m = int(input())
print(pow(a,b))
print(pow(a,b,m))


# Integers in Python can be as big as the bytes in your machine's memory. There is no limit in size as there is:  (c++ int) or  (C++ long long int).

# As we know, the result of  grows really fast with increasing .

# Let's do some calculations on very large integers.

# Task
# Read four numbers, a, b, c, and d, and print the result of a^b plus c^d

# Input Format
# Integers a, b, c, and d are given on four separate lines, respectively.

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(pow(a,b) + pow(c,d))