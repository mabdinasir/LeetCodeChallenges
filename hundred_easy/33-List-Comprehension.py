# Question 87
# Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].

# Hints: Use list comprehension to delete a bunch of element from a list.

# Solution:

li = [5,6,77,45,22,12,24]
li = [x for x in li if x%2!=0]
print(li)


# Question 88
# By using list comprehension, please write a program to print the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

# Hints: Use list comprehension to delete a bunch of element from a list.

# Solution:

li = [12,24,35,70,88,120,155]
li = [x for x in li if x%5!=0 and x%7!=0]
print(li)


# Question 89
# By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

# Hints: Use list comprehension to delete a bunch of element from a list. Use enumerate() to get (index, value) tuple.

# Solution:

li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i%2!=0]
print(li)


# Question 90
# By using list comprehension, please write a program generate a 358 3D array whose each element is 0.

# Hints: Use list comprehension to make an array.

# Solution:

array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
print(array)


# Question 91
# By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

# Hints: Use list comprehension to delete a bunch of element from a list. Use enumerate() to get (index, value) tuple.

# Solution:

li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i not in (0,4,5)]
print(li)


# Question 92
# By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

# Hints: Use list's remove method to delete a value.

# Solution:

li = [12,24,35,24,88,120,155]
li = [x for x in li if x!=24]
print(li)
