# Question 97
# Please write a program which accepts a string from console and print it in reverse order.

# Example: If the following string is given as input to the program:

# rise to vote sir

# Then, the output of the program should be:

# ris etov ot esir

# Hints: Use list[::-1] to iterate a list in a reverse order.

# Solution:

s=input("Enter a string: ")
s = s[::-1]
print(s)


# Question 98
# Please write a program which accepts a string from console and print the characters that have even indexes.

# Example: If the following string is given as input to the program:

# H1e2l3l4o5w6o7r8l9d

# Then, the output of the program should be:

# Helloworld

# Hints: Use list[::2] to iterate a list by step 2.

# Solution:

s = input("Enter a string to print even indexes:")
result = s[::2]
print(result)


# Question 99
# Please write a program which prints all permutations of [1,2,3]

# Hints: Use itertools.permutations() to get permutations of list.

# Solution:

import itertools
print(list(itertools.permutations([1,2,3])))