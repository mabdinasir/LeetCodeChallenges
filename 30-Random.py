# Question 74
# Please generate a random float where the value is between 10 and 100 using Python math module.

# Hints: Use random.random() to generate a random float in [0,1].

# Solution:

import random
print(random.random()*100)

# Question 76
# Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.

# Hints: Use random.choice() to a random element from a list.

# Solution:

import random
print(random.choice([i for i in range(11) if i%2==0]))

# Question 77
# Please write a program to output a random number, which is divisible by 5 and 7, 
# between 0 and 10 inclusive using random module and list comprehension.

# Hints: Use random.choice() to a random element from a list.
#Solution:

import random
print(random.choice([i for i in range(201) if i%5==0 and i%7==0]))

# Question 78
# Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.

# Hints: Use random.sample() to generate a list of random values.

# Solution:

import random
print(random.sample(range(100, 201), 5))

# Question 79
# Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

# Hints: Use random.sample() to generate a list of random values.

# Solution:

import random
print(random.sample([i for i in range(100,201) if i%2==0], 5))

# Question 80
# Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.

# Hints: Use random.sample() to generate a list of random values.

# Solution:

import random
print(random.sample([i for i in range(1,1001) if i%5==0 and i%7==0], 5))

# Question 81
# Please write a program to randomly print a integer number between 7 and 15 inclusive.

# Hints: Use random.randrange() to a random integer in a given range.

# Solution:

import random
print(random.randrange(7,16))